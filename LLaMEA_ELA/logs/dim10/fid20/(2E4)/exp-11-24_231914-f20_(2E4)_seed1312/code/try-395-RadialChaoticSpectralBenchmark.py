import numpy as np

class RadialChaoticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=(10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, size=10)
        
        # Chaotic perturbation parameters using logistic map
        self.chaotic_r = np.random.uniform(3.5, 4.0, size=dim)
        self.chaotic_x = np.random.uniform(0.1, 0.9, size=dim)
        
        # Spectral filtering components with varying frequencies
        self.spectral_freqs = np.random.uniform(1.0, 15.0, size=dim)
        self.spectral_amps = np.random.uniform(0.1, 2.0, size=dim)
        
        # Sharp transition regions
        self.transition_centers = np.random.uniform(-4.0, 4.0, size=dim)
        self.transition_widths = np.random.uniform(0.1, 0.5, size=dim)
        
        # Dimensional interaction weights
        self.interaction_weights = np.random.uniform(0.5, 2.0, size=(dim, dim))
        
        # Non-smooth component parameters
        self.nonsmooth_params = np.random.uniform(0.5, 3.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(10):
            dist_sq = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_component += self.rbf_widths[i] * np.exp(-dist_sq / (2.0 * 0.5**2))
        
        # Chaotic perturbation component
        chaotic_component = 0.0
        for i in range(self.dim):
            # Update chaotic map
            self.chaotic_x[i] = self.chaotic_r[i] * self.chaotic_x[i] * (1.0 - self.chaotic_x[i])
            chaotic_component += self.chaotic_x[i] * np.sin(x[i])
        
        # Spectral filtering component
        spectral_component = 0.0
        for i in range(self.dim):
            spectral_component += self.spectral_amps[i] * np.sin(self.spectral_freqs[i] * x[i])
        
        # Sharp transition component
        transition_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.transition_centers[i])
            transition_component += self.transition_widths[i] * np.exp(-dist / (2.0 * 0.2**2))
        
        # Dimensional interaction component
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_weights[i, j] * x[i] * x[j]
        
        # Non-smooth component with absolute values and power transformations
        nonsmooth_component = 0.0
        for i in range(self.dim):
            nonsmooth_component += self.nonsmooth_params[i] * (np.abs(x[i]) ** 1.5)
        
        # Combine all components
        return (1.2 * rbf_component + 
                0.8 * chaotic_component + 
                1.0 * spectral_component + 
                0.6 * transition_component + 
                0.7 * interaction_component + 
                0.9 * nonsmooth_component)