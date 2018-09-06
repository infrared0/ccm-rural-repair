sounddir = "/home/endaga/menu_sounds/"
recorddir = "/tmp/"

function goodbye ()
    session:execute("playback", sounddir .. "thankyou.wav");
    session:hangup();
end

session:answer();
while (session:ready() == true) do
    session:setAutoHangup(false);
    digits = session:playAndGetDigits(1, 1, 3, 3000, "", sounddir .. "main.wav", sounddir .. "maininvalid.wav", "[123]");
    if (digits == "") then -- no input
        goodbye();
    end

    if (digits == "1")  then   -- record audio
        my_number = session:playAndGetDigits(1, 1, 3, 3000, "", sounddir .. "record.wav", sounddir .. "recordinvalid.wav", "\\d+");
        if (my_number == "") then
            goodbye();
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
        goodbye();
    end

    if (digits == "2")  then -- listen
        my_number = session:playAndGetDigits(1, 1, 3, 3000, "", sounddir .. "listen.wav", sounddir .. "listeninvalid.wav", "\\d+");
        if (my_number == "") then
            goodbye();
        end

        filename = recorddir .. my_number .. ".wav"

        session:execute("playback",filename);
        session:sleep(100);
        goodbye();
    end

    if (digits == "3")  then
        session:execute("playback", sounddir .. "mainshort.wav");
    end
end

