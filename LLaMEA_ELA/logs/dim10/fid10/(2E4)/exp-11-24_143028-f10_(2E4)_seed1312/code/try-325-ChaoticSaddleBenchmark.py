import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map parameters for chaotic dynamics
        self.r_values = np.random.uniform(3.57, 4.0, dim)
        # Fractional Brownian motion parameters
        self.hurst = np.random.uniform(0.1, 0.9, dim)
        # Multi-scale harmonic components
        self.freq_scales = np.logspace(0, 2, 5)
        self.harmonic_amps = np.random.uniform(0.5, 2.0, (dim, len(self.freq_scales)))
        # Fractal modulation parameters
        self.fractal_dims = np.random.uniform(1.1, 2.9, dim)
        # Embedding parameters
        self.embedding_matrix = np.random.randn(dim, dim) * 0.5
        # Chaotic attractor centers
        self.attractor_centers = np.random.uniform(-2.0, 2.0, (dim, 3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize chaotic dynamics
        chaotic_state = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_values[i]
            # Logistic map iteration
            chaotic_state[i] = r * (x[i] / 5.0) * (1 - x[i] / 5.0)
            
        # Fractional Brownian motion component
        fbm_component = 0.0
        for i in range(self.dim):
            hurst = self.hurst[i]
            # Simple approximation of fractional Brownian motion using random walks
            steps = np.random.randn(10) * (x[i] / 5.0)
            fbm_component += np.sum(steps ** (2 * hurst))
            
        # Multi-scale harmonic modulation
        harmonic_sum = 0.0
        for i in range(self.dim):
            for j, freq_scale in enumerate(self.freq_scales):
                amp = self.harmonic_amps[i, j]
                harmonic_sum += amp * np.sin(freq_scale * x[i] + np.pi / 4)
                
        # Fractal geometry modulation
        fractal_mod = 0.0
        for i in range(self.dim):
            dim_factor = self.fractal_dims[i]
            fractal_mod += np.sin(x[i] ** dim_factor) * np.cos(x[i] ** (dim_factor - 0.5))
            
        # Embedding transformation
        embedded = self.embedding_matrix @ x
        
        # Attractor-based attraction term
        attractor_term = 0.0
        for i in range(self.dim):
            center_distances = np.abs(embedded[i] - self.attractor_centers[i])
            attractor_term += np.min(center_distances)
            
        # Combine all components with non-linear coupling
        fitness = (
            np.sum(chaotic_state**2) +
            0.5 * fbm_component +
            0.3 * harmonic_sum**2 +
            0.2 * fractal_mod**2 +
            0.1 * attractor_term**2 +
            0.05 * np.sum(np.sin(embedded)**2) +
            0.02 * np.sum(np.cos(embedded)**2)
        )
        
        # Add chaotic noise term
        noise = np.random.uniform(-0.01, 0.01, self.dim)
        fitness += np.sum(noise * x)
        
        return fitness