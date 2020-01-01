package main

import (
	"context"
	"encoding/json"
	firebase "firebase.google.com/go"
	"fmt"
	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
	"google.golang.org/api/iterator"
	"google.golang.org/api/option"
	"log"
	"net/http"
	"os"
)

func main() {
	e := echo.New()

	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	e.GET("/users", usersHandler())

	e.Start(":8080")
}

func firebaseInit() *firebase.App {
	opt := option.WithCredentialsFile(os.Getenv("GOOGLE_APPLICATION_CREDENTIALS"))

	app, err := firebase.NewApp(context.Background(), nil, opt)
	if err != nil {
		fmt.Println(err)
	}
	return app
}

func users() {
	ctx := context.Background()
	app := firebaseInit()
	client, err := app.Firestore(ctx)
	if err != nil {
		fmt.Println(err)
	}

	iter := client.Collection("users").Documents(ctx)
	for {
		doc, err := iter.Next()
		if err == iterator.Done {
			break
		}
		if err != nil {
			log.Fatalf("Failed to iterate: %v", err)
		}
		bytes, _ := json.Marshal(doc.Data())
		fmt.Println(string(bytes)) // TODO return JSON
	}
}

func usersHandler() echo.HandlerFunc {
	return func(c echo.Context) error {
		users() // TODO get JSON
		return c.String(http.StatusOK, "aaa")
	}
}
