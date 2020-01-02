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
	"time"
)

type Person struct {
	Age          int       `json:"age"`
	Biography    string    `json:"biography""`
	Born         string    `json:"born"`
	Followees    int       `json:"followees"`
	Followers    int       `json:"followers"`
	Intersection int       `json:"intersection"`
	IsArtist     bool      `json:"is_artist"`
	IsVerified   bool      `json:"is_verified"`
	MediaCount   int       `json:"media_count"`
	PriceAverage float64   `json:price_average`
	StoredAt     time.Time `json:"stored_at"`
	UserID       string    `json:"userid""`
}

func NewPerson(biography string) *Person {
	return &Person{Biography: biography}
}

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
		if err == iterator.Done || num == 2 {
			break
		}
		if err != nil {
			log.Fatalf("Failed to iterate: %v", err)
		}
		bytes, _ := json.Marshal(doc.Data())
		fmt.Println(doc.Data())
		var person Person
		json.Unmarshal(bytes, &person)
		fmt.Println(string(bytes)) // TODO: return JSON
		fmt.Println("document id:", doc.Ref.ID)
		fmt.Println("user_id: ", person.UserID)
		fmt.Println("media_count", person.MediaCount)
		num += 1
	}
}

func usersHandler() echo.HandlerFunc {
	return func(c echo.Context) error {
		users(0) // TODO: get JSON
		return c.String(http.StatusOK, "aaa")
	}
}
