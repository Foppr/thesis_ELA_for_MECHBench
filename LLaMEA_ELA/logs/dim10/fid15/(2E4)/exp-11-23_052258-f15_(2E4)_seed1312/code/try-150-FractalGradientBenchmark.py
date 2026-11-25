import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Generate fractal attractor points with chaotic distribution
        self.attractors = []
        for i in range(dim):
            x = 5.0 * np.sin(i * np.pi / (dim + 1)) * np.cos(i * 0.3)
            y = 5.0 * np.cos(i * np.pi / (dim + 1)) * np.sin(i * 0.4)
            self.attractors.append([x, y])
        self.attractors = np.array(self.attractors)
        
        # Fractal polynomial coefficients with recursive scaling
        self.poly_coeffs = []
        for i in range(dim):
            scale = 0.5 + 0.3 * np.sin(i * 0.7) + 0.2 * np.cos(i * 0.9)
            self.poly_coeffs.append(scale)
            
        # Enhanced gradient field parameters with fractal modulation
        self.field_strengths = []
        for i in range(dim):
            strength = 1.0 + 0.5 * np.cos(i * 0.4) + 0.3 * np.sin(i * 0.6)
            self.field_strengths.append(strength)
            
        # Fractal coupling coefficients
        self.coupling_coeffs = []
        for i in range(dim):
            coeff = 0.1 + 0.2 * np.sin(i * 0.5) * np.cos(i * 0.3)
            self.coupling_coeffs.append(coeff)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation with fractal frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(x[i]) * np.cos(x[i] / 2.0) + 
                        0.5 * np.sin(3 * x[i]) + 
                        0.3 * np.sin(5 * x[i]) * np.cos(2 * x[i]))
            
        # Fractal polynomial interaction terms
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += self.poly_coeffs[i] * (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2)
            
        # Enhanced attractor field component with fractal attraction
        attractor_term = 0.0
        for i in range(self.dim):
            dist = np.sqrt((x[i] - self.attractors[i][0])**2 + (x[i] - self.attractors[i][1])**2)
            attractor_term += self.field_strengths[i] * np.exp(-dist**2 / 3.0) * np.sin(dist * 0.5)
            
        # Fractal cross-dimensional interaction with coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_coeffs[i] * self.coupling_coeffs[j]
                cross_term += coupling * (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j])**1.5)
                
        # Fractal barrier with multi-scale oscillatory behavior
        barrier_term = 0.0
        for i in range(self.dim):
            val = x[i]
            barrier_term += (val**2 + 0.3 * np.sin(2 * val) + 0.1 * np.cos(3 * val)) * np.exp(-val**2 / 8.0)
            
        # Multi-scale fractal oscillation with varying frequencies
        freq_term = 0.0
        frequencies = [1.0, 2.0, 3.0, 4.0, 5.0]
        for freq in frequencies:
            for i in range(self.dim):
                freq_term += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0) * np.exp(-freq**2 / 10.0)
                
        # Fractal dimension scaling with chaotic modulation
        dim_factor = 1.0 + 0.4 * np.log(self.dim + 1) + 0.2 * np.sum(np.abs(x)**3.0)
        dim_factor *= (1.0 + 0.1 * np.sin(np.sum(x) * 0.3))
        
        # Combine all terms with fractal weights
        weights = [0.20, 0.25, 0.18, 0.22, 0.15]
        total = (weights[0] * sin_term + 
                weights[1] * poly_term + 
                weights[2] * attractor_term + 
                weights[3] * cross_term + 
                weights[4] * barrier_term)
                
        return dim_factor * total