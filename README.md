# PDF_Clause_Detector
A codeless solution for labelling, training and inference on PDFs

Steps:
1. Start Grobid server 
```
docker pull lfoppiano/grobid:0.6.2
docker run -t --rm --init -p 8070:8070 -p 8081:8071 lfoppiano/grobid:0.6.2
```
2. Start react App
```
cd ui/ui
npm start
```

To do:
- Use Grobid to get segmented xml, store as pdf and DataFrame, display pdf