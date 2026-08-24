import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base harmonic potential with time-varying frequency
        f = 0.0
        t = 0.5 * (np.sum(x**2) / self.dim + 1.0)
        
        # Chaotic modulation of harmonic frequencies
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(t + i * 0.3) + 0.3 * np.cos(t * 0.7 + i * 0.5)
            f += 0.5 * freq * x[i]**2
        
        # Add chaotic saddle points with varying depths
        saddle_sum = 0
        for i in range(self.dim):
            # Time-varying saddle structure
            saddle_depth = 1.0 + 0.5 * np.sin(t * 1.3 + i * 0.4)
            saddle_freq = 2.0 + 0.8 * np.cos(t * 0.9 + i * 0.6)
            saddle_sum += saddle_depth * np.sin(x[i] * saddle_freq) * np.cos(x[i] * 0.5)
        f += 1.2 * saddle_sum
        
        # Add discontinuous gradient regions
        discontinuity_sum = 0
        for i in range(self.dim):
            # Piecewise linear discontinuity with chaotic switching
            switch = np.sin(t * 2.0 + i * 0.8)
            if switch > 0:
                discontinuity_sum += x[i]**3
            else:
                discontinuity_sum += x[i]**4
        f += 0.8 * discontinuity_sum
        
        # Multi-scale harmonic interactions
        multi_harmonic = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling strength
                coupling = 0.5 + 0.3 * np.sin(t * 0.6 + i * 0.4 + j * 0.3)
                multi_harmonic += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        f += 1.0 * multi_harmonic
        
        # Add chaotic gradient modulation
        gradient_mod = 0
        for i in range(self.dim):
            # Chaotic modulation of gradient magnitude
            mod = 1.0 + 0.4 * np.sin(t * 1.2 + x[i] * 0.5)
            gradient_mod += mod * np.sin(x[i] * 2.0 + np.sin(x[i] * 3.0))
        f += 0.6 * gradient_mod
        
        # Add fractal-like boundary interactions
        boundary_interaction = 0
        for i in range(self.dim):
            # Boundary-dependent harmonic terms
            boundary_dist = min(abs(x[i] - 5.0), abs(x[i] + 5.0))
            boundary_interaction += 0.3 * np.sin(boundary_dist * 1.5) * x[i]**2
        f += 0.7 * boundary_interaction
        
        # Add time-varying noise with chaotic pattern
        noise = 0
        for i in range(self.dim):
            noise += np.sin(t * 3.0 + x[i] * 2.5 + np.sin(x[i] * 4.0))
        f += 0.4 * noise
        
        # Add higher-order polynomial terms for increased complexity
        poly_terms = 0
        for i in range(self.dim):
            poly_terms += 0.1 * x[i]**5 + 0.2 * x[i]**6
        f += 0.5 * poly_terms
        
        # Add global structure with time-varying harmonic minima
        global_minima = 0
        for i in range(15):
            # Chaotic minima positions
            pos = 4.0 * np.sin(t * 0.5 + i * 0.4)
            amplitude = 1.0 + 0.3 * np.cos(t * 0.7 + i * 0.3)
            global_minima += amplitude * np.exp(-0.5 * (x[0] - pos)**2)
        f += 1.5 * global_minima
        
        return f