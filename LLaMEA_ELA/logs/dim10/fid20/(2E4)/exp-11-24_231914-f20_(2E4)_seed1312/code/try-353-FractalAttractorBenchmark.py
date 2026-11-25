import numpy as np

class FractalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Iterated Function System parameters for fractal generation
        self.ifs_probabilities = np.random.dirichlet(np.ones(4), size=dim).T
        self.ifs_affine = np.random.uniform(-1.5, 1.5, size=(dim, 4, 2, 2))
        self.ifs_translations = np.random.uniform(-2.0, 2.0, size=(dim, 4, 2))
        
        # Spectral decomposition components
        self.spectral_freq = np.random.uniform(0.5, 8.0, size=dim)
        self.spectral_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.spectral_phase = np.random.uniform(0.0, 2*np.pi, size=dim)
        
        # Dynamic attractor field parameters
        self.attractor_centers = np.random.uniform(-4.0, 4.0, size=(15, dim))
        self.attractor_strengths = np.random.uniform(1.0, 5.0, size=15)
        self.attractor_radii = np.random.uniform(0.5, 3.0, size=15)
        self.attractor_damping = np.random.uniform(0.1, 2.0, size=15)
        
        # Fractal dimension and scaling parameters
        self.fractal_dims = np.random.uniform(1.1, 2.9, size=dim)
        self.scale_factors = np.random.uniform(0.5, 2.0, size=dim)
        
        # Time-varying components for dynamic landscape
        self.time_freq = np.random.uniform(0.1, 0.8, size=dim)
        self.time_amp = np.random.uniform(0.1, 1.0, size=dim)
        
        # Connectivity and basin interaction parameters
        self.basin_connectivity = np.random.uniform(0.1, 0.9, size=(15, 15))
        self.basin_stability = np.random.uniform(0.2, 1.0, size=15)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal iterated function system component
        ifs_component = 0.0
        for i in range(self.dim):
            point = np.array([x[i], 0.0])
            for _ in range(100):  # Apply IFS iterations
                rand_idx = np.random.choice(4, p=self.ifs_probabilities[i])
                affine = self.ifs_affine[i, rand_idx]
                translation = self.ifs_translations[i, rand_idx]
                point = affine @ point + translation
            ifs_component += np.linalg.norm(point)
            
        # Spectral decomposition component
        spectral_component = 0.0
        for i in range(self.dim):
            freq = self.spectral_freq[i]
            amp = self.spectral_amp[i]
            phase = self.spectral_phase[i]
            spectral_component += amp * np.sin(freq * x[i] + phase)
            
        # Dynamic attractor field component
        attractor_component = 0.0
        for j in range(15):
            dist = np.linalg.norm(x - self.attractor_centers[j])
            if dist < self.attractor_radii[j]:
                influence = (self.attractor_strengths[j] * 
                           np.exp(-dist**2 / (2 * self.attractor_damping[j]**2)) *
                           self.attractor_stability[j])
                attractor_component += influence
                
        # Fractal dimension scaling component
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_val = self.fractal_dims[i] * np.log(1 + np.abs(x[i]))
            fractal_component += fractal_val
            
        # Time-varying modulation
        time_component = 0.0
        for i in range(self.dim):
            time_val = self.time_amp[i] * np.sin(self.time_freq[i] * x[i])
            time_component += time_val
            
        # Basin connectivity and interaction
        basin_component = 0.0
        for j in range(15):
            dist = np.linalg.norm(x - self.attractor_centers[j])
            if dist < self.attractor_radii[j]:
                # Connectivity weight from other basins
                conn_weight = 0.0
                for k in range(15):
                    if j != k:
                        conn_dist = np.linalg.norm(self.attractor_centers[j] - self.attractor_centers[k])
                        conn_weight += self.basin_connectivity[j, k] * np.exp(-conn_dist**2 / 10.0)
                basin_component += (self.attractor_strengths[j] * 
                                  (1 - dist / self.attractor_radii[j]) * 
                                  conn_weight * self.attractor_stability[j])
                
        # Combine all components with appropriate weights
        return (1.5 * ifs_component + 
                1.2 * spectral_component + 
                1.0 * attractor_component + 
                0.8 * fractal_component + 
                0.6 * time_component + 
                0.4 * basin_component)