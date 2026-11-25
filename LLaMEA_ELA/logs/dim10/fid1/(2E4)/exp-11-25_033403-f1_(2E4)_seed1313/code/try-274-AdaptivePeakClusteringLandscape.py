import numpy as np

class AdaptivePeakClusteringLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (6, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.5, 6)
        self.rbf_heights = np.random.uniform(1.0, 5.0, 6)
        # Initialize peak clustering parameters
        self.clusters = np.random.randint(2, 5, dim)
        self.cluster_centers = np.random.uniform(-3.0, 3.0, (6, dim))
        self.cluster_radii = np.random.uniform(1.0, 3.0, 6)
        # Initialize dynamic gradient modulation
        self.modulation_freqs = np.random.uniform(0.5, 3.0, dim)
        self.modulation_amplitudes = np.random.uniform(0.1, 1.0, dim)
        self.modulation_phases = np.random.uniform(0, 2*np.pi, dim)
        # Initialize adaptive scaling
        self.scaling_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial basis function potential
        rbf_potential = 0.0
        for i in range(6):
            dist = 0.0
            for j in range(self.dim):
                dist += ((x[j] - self.rbf_centers[i, j]) / self.rbf_widths[i])**2
            rbf_potential += self.rbf_heights[i] * np.exp(-0.5 * dist)
            
        # Add peak clustering effects
        cluster_potential = 0.0
        for i in range(6):
            dist = 0.0
            for j in range(self.dim):
                dist += ((x[j] - self.cluster_centers[i, j]) / self.cluster_radii[i])**2
            if dist <= 1.0:
                cluster_potential += np.exp(-dist)
                
        # Add dynamic gradient modulation
        modulation = 0.0
        for j in range(self.dim):
            modulation += self.modulation_amplitudes[j] * np.sin(self.modulation_freqs[j] * x[j] + self.modulation_phases[j])
            
        # Add adaptive scaling terms
        scaling_terms = 0.0
        for j in range(self.dim):
            scaling_terms += self.scaling_factors[j] * (x[j]**2) * np.cos(x[j])
            
        # Combine all components with varying weights
        total = 0.3 * rbf_potential + 0.4 * cluster_potential + 0.2 * modulation + 0.1 * scaling_terms
        
        return total