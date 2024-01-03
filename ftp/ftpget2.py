import ftplib

FTP = {
    "PATH": 'C:\Program Files',
    "FILENAME": 'SHA256SUMS',
    "URL": 'ftp.heanet.ie'
}

# Make the connection
ftp = ftplib.FTP(FTP['URL'])
# Anonymous login
ftp.login() 
# Change to the correct directory
ftp.cwd(FTP["PATH"])
# Retrieve the file
ftp.retrbinary("RETR " + FTP["FILENAME"], open(FTP["FILENAME"], 'wb').write)
ftp.quit()
