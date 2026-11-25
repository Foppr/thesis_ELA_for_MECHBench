import numpy as np

class GaussianRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define number of mixture components
        self.n_components = 5 + dim // 2
        # Randomly initialize component centers within [-5, 5]
        self.centers = np.random.uniform(-5.0, 5.0, (self.n_components, dim))
        # Randomly initialize variances for each component
        self.variances = np.random.uniform(0.5, 2.0, self.n_components)
        # Randomly initialize weights for each component
        self.weights = np.random.uniform(0.5, 2.0, self.n_components)
        # Normalize weights
        self.weights = self.weights / np.sum(self.weights)
        # Adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture component
        gaussian_term = 0.0
        for i in range(self.n_components):
            diff = x - self.centers[i]
            # Apply adaptive conditioning
            weighted_diff = diff * self.conditioning_factors
            exponent = -0.5 * np.sum(weighted_diff**2 / self.variances[i])
            gaussian_term += self.weights[i] * np.exp(exponent)
            
        # Radial basis function interactions
        rbf_term = 0.0
        for i in range(self.n_components):
            diff = x - self.centers[i]
            # Use squared exponential RBF
            rbf_value = np.exp(-np.sum(diff**2) / (2 * self.variances[i]**2))
            rbf_term += self.weights[i] * rbf_value
            
        # Cross-dimensional coupling via polynomial terms
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                poly_coupling += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                
        # Asymmetric basin terms with varying depths
        basin_term = 0.0
        for i in range(self.dim):
            # Varying basin depths and asymmetries
            depth = 1.0 + 0.3 * np.sin(0.5 * i)
            asymmetry = 0.2 * np.cos(0.7 * i)
            basin_term += depth * (np.tanh(x[i] - asymmetry) * x[i]**3)
            
        # Multi-scale harmonic modulation
        harmonic_term = 0.0
        freqs = [1.0, 2.0, 3.0, 4.0]
        for i in range(self.dim):
            for freq in freqs:
                harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
                
        # Combine all terms with carefully balanced weights
        weights = [0.25, 0.20, 0.20, 0.20, 0.15]
        total = (weights[0] * gaussian_term + 
                weights[1] * rbf_term + 
                weights[2] * poly_coupling + 
                weights[3] * basin_term + 
                weights[4] * harmonic_term)
                
        # Add dimensionality-based scaling
        scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sum(np.abs(x)**1.2)
        
        return scale * total