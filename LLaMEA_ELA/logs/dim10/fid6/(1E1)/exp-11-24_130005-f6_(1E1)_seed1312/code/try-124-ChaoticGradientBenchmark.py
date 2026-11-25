import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic dynamics
        self.c1 = 3.8
        self.c2 = 0.9
        self.c3 = 2.0
        
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Base quadratic term with time-varying coefficients
        base_quad = np.sum(x_scaled**2)
        
        # Chaotic gradient component using iterated sine maps
        chaotic_grad = 0.0
        for i in range(self.dim):
            x_chaos = 0.5
            for _ in range(10):
                x_chaos = self.c1 * x_chaos * (1 - x_chaos)
            # Apply time-varying modulation based on chaotic dynamics
            mod = np.sin(self.c2 * x_chaos + x_scaled[i]) * np.cos(self.c3 * x_chaos * x_scaled[i])
            chaotic_grad += mod * x_scaled[i]**2
        
        # Saddle-point structure with multiple interacting potentials
        saddle_term = 0.0
        for i in range(self.dim):
            # Create a combination of attractive and repulsive forces
            saddle_term += (x_scaled[i]**4 - 2*x_scaled[i]**2) * np.cos(3.0 * x_scaled[i])
        
        # Fractal-like component using fractional Brownian motion approximation
        fractal = 0.0
        for i in range(self.dim):
            # Use multiple sine waves with increasing frequencies
            freqs = [1.0, 2.5, 4.0, 6.0]
            for f in freqs:
                fractal += np.sin(f * x_scaled[i]) * (1.0 / (f + 1.0))
        
        # Time-varying harmonic component
        time_vary = 0.0
        for i in range(self.dim):
            time_vary += np.sin(2.0 * x_scaled[i] + np.cos(x_scaled[i])) * \
                        np.cos(3.0 * x_scaled[i] + np.sin(x_scaled[i]))
        
        # Cross-dimensional coupling with dynamic weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                weight = np.sin(x_scaled[i] + x_scaled[j])
                cross_coupling += weight * (x_scaled[i]**2 + x_scaled[j]**2)
        
        # Combine all terms with dynamic scaling
        return 0.5 * base_quad + 1.2 * chaotic_grad + 0.8 * saddle_term + \
               0.6 * fractal + 0.7 * time_vary + 0.4 * cross_coupling