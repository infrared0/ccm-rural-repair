sounddir = "/home/endaga/menu_sounds/"
recorddir = "/tmp/"

session:answer();
while (session:ready() == true) do
    session:setAutoHangup(false);
    digits = session:playAndGetDigits(1, 1, 3, 3000, "", sounddir .. "main.wav", sounddir .. "maininvalid.wav", "[123]");

    if (digits == "1")  then   -- record audio
        session:execute("playback", sounddir .. "record.wav");

        -- get digit to be used as filename
        my_number = session:getDigits(1, "", 3000);
        while (my_number == "" or my_number == "#" or my_number == "*") do
            session:sleep(100);
            my_number = session:getDigits(1, "", 3000);
        end   
        session:execute("playback", sounddir .. "beep.wav");
        session:sleep(100);
	
        -- do the actual recording. will terminate if silent for 5 seconds
        filename = recorddir .. my_number .. ".wav"
        session:recordFile(filename, 1200, 200, 5);
        session:sleep(100);
        session:execute("playback", sounddir .. "beep.wav");
        session:sleep(100);
        session:execute("playback", filename);
        session:sleep(100);

        -- send your infomational SMS about the recording
        session:execute("python", "VBTS_Send_SMS ${vbts_callerid}|2910|Your recording number is " .. my_number .. ". Enter this number to listen to recording");

        session:execute("playback", sounddir .. "thankyou.wav");
        session:sleep(50);
        session:hangup();
    end
    if (digits == "2")  then -- listen
        session:execute("playback", sounddir .. "listen_recording.wav");
        session:sleep(100);

        -- get recording number
        my_number = session:getDigits(1, "", 3000);
        while (my_number == "") do
            session:sleep(3000);
            my_number = session:getDigits(1, "", 3000);
        end   
        filename = recorddir .. my_number .. ".wav"

        session:execute("playback",filename);
        session:sleep(100);
        session:execute("playback", sounddir .. "thankyou.wav");
        session:sleep(50);
        session:hangup();
    end

    if (digits == "3")  then
        session:execute("playback", sounddir .. "mainshort.wav");
    end
end
