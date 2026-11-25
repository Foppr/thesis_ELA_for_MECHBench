import numpy as np

class RadialPeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute periodic parameters
        self.freqs = 2.0 + 1.5 * np.sin(np.arange(dim) * 0.7)
        self.amps = 1.0 + 0.8 * np.cos(np.arange(dim) * 0.5)
        self.radial_coeffs = 0.5 + 0.3 * np.random.rand(dim)
        # Exponential conditioning parameters
        self.exp_params = 1.2 + 0.6 * np.sin(np.arange(dim) * 0.9)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial term with periodic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 * np.exp(-0.1 * r) * (1.0 + 0.3 * np.sin(r * 0.5))
        
        # Periodic multimodal term
        periodic_term = 0.0
        for i in range(self.dim):
            # Combine sine and cosine with amplitude and frequency modulation
            term = self.amps[i] * (np.sin(self.freqs[i] * x[i]) + np.cos(self.freqs[i] * x[i]))
            periodic_term += term**2
        
        # Cross-dimensional coupling with radial dependence
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Radial-dependent coupling strength
                coupling_strength = 0.3 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                coupling_term += coupling_strength * np.sin(x[i] - x[j])**2
        
        # Exponentially conditioned term
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += self.exp_params[i] * np.exp(0.1 * x[i]**2) * x[i]**4
        
        # Add radial symmetry breaking noise
        noise = 0.1 * np.sum(np.sin(x * 3.0) * np.cos(x * 2.0))
        
        return radial_term + periodic_term + coupling_term + exp_term + noise