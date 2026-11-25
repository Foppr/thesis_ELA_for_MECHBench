import numpy as np

class SinusoidalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate attractor points with enhanced sinusoidal distribution
        self.attractors = []
        for i in range(dim):
            x = 5.0 * np.sin(i * np.pi / (dim + 2))
            y = 5.0 * np.cos(i * np.pi / (dim + 2))
            self.attractors.append([x, y])
        self.attractors = np.array(self.attractors)
        
        # Enhanced polynomial interaction coefficients
        self.poly_coeffs = []
        for i in range(dim):
            self.poly_coeffs.append(0.7 + 0.3 * np.sin(i * 0.8))
            
        # Adaptive gradient field parameters
        self.field_strengths = [1.2 + 0.4 * np.cos(i * 0.5) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation component
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(x[i]) * np.cos(x[i] / 2.0) + 
                        0.5 * np.sin(3 * x[i]) + 
                        0.3 * np.sin(5 * x[i]))
            
        # Modified polynomial interaction terms
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += self.poly_coeffs[i] * (x[i]**4 + 0.6 * x[i]**3 + 0.3 * x[i]**2)
            
        # Enhanced attractor field component with adaptive attraction
        attractor_term = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.attractors[i][0])
            attractor_term += self.field_strengths[i] * np.exp(-dist**2 / 3.0)
            
        # Improved cross-dimensional interaction with asymmetric coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1.0 + 0.5 * np.abs(x[i] - x[j])**1.5)
                
        # Enhanced barrier term with multi-frequency oscillation
        barrier_term = 0.0
        for i in range(self.dim):
            val = x[i]
            barrier_term += (val**2 + 0.4 * np.sin(2 * val) + 0.2 * np.sin(4 * val)) * np.exp(-val**2 / 8.0)
            
        # Multi-scale oscillation with adaptive frequencies
        freq_term = 0.0
        frequencies = [1.0, 2.0, 3.0, 4.0, 5.0]
        for freq in frequencies:
            for i in range(self.dim):
                freq_term += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0) * np.exp(-freq**2 / 20.0)
                
        # Combine all terms with improved weighting scheme
        weights = [0.30, 0.25, 0.18, 0.15, 0.12]
        total = (weights[0] * sin_term + 
                weights[1] * poly_term + 
                weights[2] * attractor_term + 
                weights[3] * cross_term + 
                weights[4] * barrier_term)
                
        # Enhanced dimensionality scaling with adaptive component
        scale = 1.0 + 0.4 * np.log(self.dim + 1) + 0.2 * np.sum(np.abs(x)**3.0)
        
        return scale * total