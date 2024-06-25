package duckdb

import (
	"database/sql"
	"errors"
	"log"

	_ "github.com/marcboeker/go-duckdb"
)

type People struct {
	id   int
	name string
}

func GetSampleData() (int, string) {
	db, err := sql.Open("duckdb", "")
	if err != nil {
		log.Fatal(err)
	}

	defer db.Close()

	_, err = db.Exec("CREATE TABLE People (id INTEGER, name VARCHAR)")
	if err != nil {
		log.Fatal(err)
	}

	_, err = db.Exec("INSERT INTO People VALUES (42, 'Jason')")
	if err != nil {
		log.Fatal(err)
	}

	// We now will try to read these values
	var (
		id   int
		name string
	)

	row := db.QueryRow("SELECT id, name FROM People")

	// scanning the values
	err = row.Scan(&id, &name)
	if errors.Is(err, sql.ErrNoRows) {
		log.Println("no rows")
	} else if err != nil {
		log.Fatal(err)
	}

	return id, name //People{id: id, name: name}
}
