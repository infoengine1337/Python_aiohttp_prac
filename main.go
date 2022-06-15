package main

import (
	"fmt"
	"log"
	"net/http"
)

func donate_ukraine() {

	dest_url := "http:localhost:8080"

	resp, err := http.Get(dest_url)
	defer resp.Body.Close()

	if err != nil {
		log.Fatal(err)
		return
	}

	fmt.Printf("%d", resp.StatusCode)

}

func main() {

	for i := 0; i <= 10; i++ {

		go donate_ukraine()
	}

	fmt.Printf("done")
}
