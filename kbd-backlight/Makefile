pkgname=kbd-backlight


help:
	echo "make it's alive!"

build:
	go build -o bin/${pkgname} golang/kbd-backlight.go

install:
	cp ${pkgname}.init /etc/init.d/${pkgname}
	cp ${pkgname}.service /etc/systemd/system/${pkgname}.service
	cp bin/${pkgname} /usr/local/bin/${pkgname}


clean:
	rm -r ./bin/
