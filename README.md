# Microsoft Fabric Workspace Repository

Welcome to the GitHub repository for this Microsoft Fabric workspace. This repository contains the **semantic models, pipelines, notebooks, and workspace metadata** necessary for collaboration, version control, and deployment.  

> **Note:** No actual data values are included in this repository. All files reflect structure, definitions, and configurations only.

---

## Repository Structure
MyFabricWorkspace/
├─ models/ # Semantic model definitions
├─ pipelines/ # Data pipelines and transformations
├─ notebooks/ # Notebooks for analysis and experimentation
├─ cache.mbf # Fabric sync metadata (DO NOT DELETE)
├─ README.md # This file


- **models/** – Contains JSON definitions of tables, measures, and dimensions.  
- **pipelines/** – Contains pipeline configurations and transformation logic.  
- **notebooks/** – Contains notebooks for data exploration, analytics, and reporting.  
- **cache.mbf** – Tracks sync state between the Fabric workspace and GitHub.

---

## Git Usage

- **Commit metadata, models, and pipelines** only.  
- **Do not commit actual data files**; these are excluded via `.gitignore`.  
- Keep `cache.mbf` tracked to ensure Fabric sync works properly.

---

## Contributing

1. Clone this repository.
2. Make changes to **models, pipelines, or notebooks** in Fabric.
3. Commit changes to GitHub.
4. Push updates for review or collaboration.
5. Pull updates regularly to stay in sync with the workspace.

---

## Notes

- Ensure your **GitHub Personal Access Token (PAT)** is set up in Fabric for syncing.  
- The repository is **metadata-only** to keep sensitive data secure.  
- Follow workspace conventions for naming and structuring new models, pipelines, or notebooks.

---

## Contact / Support

For questions or support regarding this repository or the Fabric workspace, contact the workspace admin or the data engineering team.
