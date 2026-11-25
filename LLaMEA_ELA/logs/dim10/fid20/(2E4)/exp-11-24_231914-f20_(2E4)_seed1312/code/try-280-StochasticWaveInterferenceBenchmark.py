import numpy as np

class StochasticWaveInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Gaussian mixture model parameters
        self.n_components = 5
        self.gmm_means = np.random.uniform(-4.0, 4.0, size=(self.n_components, dim))
        self.gmm_covs = np.array([np.eye(dim) * np.random.uniform(0.5, 2.0) for _ in range(self.n_components)])
        self.gmm_weights = np.random.dirichlet(np.ones(self.n_components))
        
        # Trigonometric wave interference patterns
        self.wave_freqs = np.random.uniform(1.0, 6.0, size=dim)
        self.wave_amps = np.random.uniform(0.5, 3.0, size=dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Adaptive noise scaling
        self.noise_scale = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_freq = np.random.uniform(0.5, 3.0, size=dim)
        
        # Dynamic optima shifting
        self.optima_shift_magnitude = np.random.uniform(1.0, 3.0)
        self.shift_frequency = np.random.uniform(0.1, 0.5)
        
    def f(self, x):
        # Normalize input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture model component
        gmm_component = 0.0
        for i in range(self.n_components):
            diff = x - self.gmm_means[i]
            exponent = -0.5 * np.dot(diff, np.linalg.solve(self.gmm_covs[i], diff))
            gmm_component += self.gmm_weights[i] * np.exp(exponent)
        
        # Trigonometric wave interference component
        wave_component = 0.0
        for i in range(self.dim):
            wave_val = self.wave_amps[i] * np.sin(self.wave_freqs[i] * x[i] + self.wave_phases[i])
            wave_component += wave_val
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_scale[i] * np.sin(self.noise_freq[i] * x[i])
            noise_component += noise_val
            
        # Dynamic optima shifting (time-dependent)
        shift = self.optima_shift_magnitude * np.sin(self.shift_frequency * np.sum(x))
        
        # Combine all components with varying weights
        return (2.0 * gmm_component + 
                1.5 * wave_component + 
                0.8 * noise_component + 
                0.5 * shift)