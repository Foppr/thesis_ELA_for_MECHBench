import numpy as np

class LogarithmicWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dynamic parameters for varying interaction strengths
        self.coupling_strengths = [0.5 + 0.3 * np.sin(i * 0.6) for i in range(dim)]
        self.wave_frequencies = [1.0 + 0.8 * np.cos(i * 0.4) for i in range(dim)]
        self.barrier_centers = [np.random.uniform(-4, 4) for _ in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier component with variable center and strength
        barrier_term = 0.0
        for i in range(self.dim):
            center = self.barrier_centers[i]
            strength = 2.0 + 1.5 * np.sin(0.7 * i)
            # Modified logarithmic barrier function
            barrier_term += strength * np.log(1.0 + (x[i] - center)**2)
            
        # Fractional polynomial interactions with dynamic exponents
        poly_term = 0.0
        for i in range(self.dim):
            # Dynamic fractional exponents based on position and index
            exponent = 1.5 + 0.5 * np.cos(x[i] * 0.5)
            poly_term += (x[i]**exponent) * (1.0 + 0.2 * np.sin(i))
            
        # Trigonometric wave pattern with adaptive frequencies
        wave_term = 0.0
        for i in range(self.dim):
            freq = self.wave_frequencies[i % len(self.wave_frequencies)]
            wave_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Cross-dimensional coupling with adaptive weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = self.coupling_strengths[i % len(self.coupling_strengths)]
                coupling_term += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Dynamic scaling factor based on dimensionality and position
        scale_factor = 1.0 + 0.25 * np.log(self.dim + 1) + 0.1 * np.sum(np.abs(x)**1.5)
        
        # Combine all terms with modified weights
        weights = [0.30, 0.25, 0.20, 0.25]  # Changed weight distribution
        total = (weights[0] * barrier_term + 
                weights[1] * poly_term + 
                weights[2] * wave_term + 
                weights[3] * coupling_term)
                
        return scale_factor * total