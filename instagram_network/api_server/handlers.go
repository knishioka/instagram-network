package main

import (
	"context"
	"encoding/json"
	firebase "firebase.google.com/go"
	"fmt"
	"github.com/labstack/echo"
	"google.golang.org/api/iterator"
	"google.golang.org/api/option"
	"log"
	"net/http"
	"os"
	"time"
)

type Person struct {
	Age          int       `firestore:"age"`
	Biography    string    `firestore:"biography""`
	Born         string    `firestore:"born"`
	Followees    int       `firestore:"followees"`
	Followers    int       `firestore:"followers"`
	Intersection int       `firestore:"intersection"`
	IsArtist     bool      `firestore:"is_artist"`
	IsVerified   bool      `firestore:"is_verified"`
	MediaCount   int       `firestore:"media_count"`
	PriceAverage float64   `firestore:"price_average""`
	StoredAt     time.Time `firestore:"stored_at"`
	UserID       int64     `firestore:"userid"`
}

func firebaseInit() *firebase.App {
	opt := option.WithCredentialsFile(os.Getenv("GOOGLE_APPLICATION_CREDENTIALS"))
	app, err := firebase.NewApp(context.Background(), nil, opt)
	if err != nil {
		fmt.Println(err)
	}
	return app
}

func users(num int) {
	ctx := context.Background()
	app := firebaseInit()
	client, err := app.Firestore(ctx)
	if err != nil {
		fmt.Println(err)
	}

	iter := client.Collection("users").Documents(ctx)
	for {
		doc, err := iter.Next()
		if err == iterator.Done || num == 4 {
			break
		}
		if err != nil {
			log.Fatalf("Failed to iterate: %v", err)
		}
		bytes, _ := json.Marshal(doc.Data()) // FIXME: Unparsable map
		fmt.Println("doc.Data():\t", doc.Data())
		fmt.Println("JSON:\t", string(bytes))
		var person Person
		doc.DataTo(&person)
		// json.Unmarshal(bytes, &person)
		// fmt.Println(string(bytes)) // TODO: return JSON
		fmt.Println("document id:\t", doc.Ref.ID)
		fmt.Println("user_id:\t", person.UserID)
		fmt.Println("media_count:\t", person.MediaCount)
		fmt.Println("stored_at:\t", person.StoredAt)
		num += 1
	}
}

func fetch_user(user_id string) {
	ctx := context.Background()
	app := firebaseInit()
	client, err := app.Firestore(ctx)
	if err != nil {
		fmt.Println(err)
	}
	user, _ := client.Collection("users").Doc(user_id).Get(ctx)
	fmt.Println(user.Data())
}

func usersHandler() echo.HandlerFunc {
	return func(c echo.Context) error {
		users(0) // TODO: get JSON
		return c.String(http.StatusOK, "OK")
	}
}

func userHandler() echo.HandlerFunc {
	return func(c echo.Context) error {
		user_id := c.Param("user_id")
		fetch_user(user_id)
		return c.String(http.StatusOK, "OK")
	}
}
