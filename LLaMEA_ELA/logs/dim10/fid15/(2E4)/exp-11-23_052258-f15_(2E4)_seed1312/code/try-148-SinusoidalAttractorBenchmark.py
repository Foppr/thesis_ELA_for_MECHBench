import numpy as np

class SinusoidalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate fractal-like attractor points with enhanced complexity
        self.attractors = []
        for i in range(dim):
            x = 5.0 * np.sin(i * np.pi / (dim + 1)) * np.cos(i * 0.5)
            y = 5.0 * np.cos(i * np.pi / (dim + 1)) * np.sin(i * 0.3)
            self.attractors.append([x, y])
        self.attractors = np.array(self.attractors)
        
        # Enhanced polynomial interaction coefficients with fractal scaling
        self.poly_coeffs = []
        for i in range(dim):
            self.poly_coeffs.append(0.8 + 0.4 * np.sin(i * 0.7) * np.cos(i * 0.3))
            
        # Modified gradient field parameters with chaotic behavior
        self.field_strengths = [1.5 + 0.8 * np.cos(i * 0.4 + np.sin(i * 0.2)) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation component with fractal frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(x[i]) * np.cos(x[i] / 2.0) + 
                        0.5 * np.sin(3 * x[i]) + 
                        0.3 * np.sin(5 * x[i]) * np.cos(2 * x[i]))
            
        # Enhanced polynomial interaction terms with higher order components
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += self.poly_coeffs[i] * (x[i]**4 + 0.7 * x[i]**3 + 0.5 * x[i]**2)
            
        # Enhanced attractor field component with multi-scale attraction
        attractor_term = 0.0
        for i in range(self.dim):
            dist1 = np.abs(x[i] - self.attractors[i][0])
            dist2 = np.abs(x[i] - self.attractors[i][1])
            attractor_term += (self.field_strengths[i] * 
                             (np.exp(-dist1**2 / 2.0) + 0.5 * np.exp(-dist2**2 / 3.0)))
            
        # Enhanced cross-dimensional interaction with fractal coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j])**1.5)
                
        # Enhanced asymmetric barrier with fractal oscillatory behavior
        barrier_term = 0.0
        for i in range(self.dim):
            val = x[i]
            barrier_term += ((val**2 + 0.3 * np.sin(2 * val) + 0.1 * np.sin(5 * val)) * 
                           np.exp(-val**2 / 8.0))
            
        # Enhanced multi-scale oscillation with chaotic frequency modulation
        freq_term = 0.0
        frequencies = [1.0, 2.0, 3.0, 4.0, 5.0]
        for freq in frequencies:
            for i in range(self.dim):
                freq_term += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0) * np.sin(freq * 0.3)
                
        # Enhanced combined terms with fractal dimension scaling
        weights = [0.20, 0.18, 0.17, 0.22, 0.23]
        total = (weights[0] * sin_term + 
                weights[1] * poly_term + 
                weights[2] * attractor_term + 
                weights[3] * cross_term + 
                weights[4] * barrier_term)
                
        # Enhanced multi-scale frequency modulation with fractal behavior
        scale = 1.0 + 0.5 * np.log(self.dim + 1) + 0.2 * np.sum(np.abs(x)**3.0) + 0.1 * np.sin(self.dim * 0.5)
        
        return scale * total