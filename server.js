const express = require('express');
const app = express();
const fs = require('fs');
app.get('/metals', (req, res) => {
  fs.readFile('nested_data.json', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: 'Internal Server Error' });
    }
    const metals = JSON.parse(data);
    const metal = metals["Elements"];
    if (metal) {
      res.json(metal);
    } else {
      res.status(404).json({ error: 'Metal not found' });
    }
  });
});

app.get('/metals/:metalName', (req, res) => {
    const metalName = req.params.metalName;
    fs.readFile('nested_data.json', 'utf8', (err, data) => {
      if (err) {
        console.error(err);
        return res.status(500).json({ error: 'Internal Server Error' });
      }
      const metals = JSON.parse(data);
      const metal = metals[metalName];
      if (metal) {
        res.json(metal);
      } else {
        res.status(404).json({ error: 'Metal not found' });
      }
    });
  });
  
  
const port = 3000;

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
