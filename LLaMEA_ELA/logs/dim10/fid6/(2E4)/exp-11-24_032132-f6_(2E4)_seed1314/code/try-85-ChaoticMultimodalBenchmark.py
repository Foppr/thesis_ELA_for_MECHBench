import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.a = 4.5
        self.b = 5.5
        self.c = 3.5
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term with higher degree and increased curvature
        poly_term = np.sum(x**8) * 0.035
        
        # Trigonometric modulations with enhanced frequency and amplitude
        trig_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple sine and cosine components with different frequencies and amplitudes
            trig_term += (np.sin(xi * self.a) * np.cos(xi * self.b) + 
                         np.sin(xi * self.c) * np.cos(xi * self.a) + 
                         np.sin(xi * self.b) * np.cos(xi * self.c)) * np.exp(-0.18 * xi**2)
        
        # Exponential interaction terms with increased complexity and stronger coupling
        exp_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                exp_term += np.exp(-0.5 * diff**2) * np.sin(x[i] + x[j]) * (x[i]**4 + x[j]**4 + 0.5 * x[i]*x[j])
        
        # Chaotic component using a modified logistic map with increased nonlinearity
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply a chaotic sine map with parameter control and additional nonlinearities
            chaotic_component = np.sin(xi * np.pi) * np.exp(-0.25 * xi**2) + 0.5 * np.sin(4 * xi)
            chaotic_term += chaotic_component * np.cos(xi * self.b + i * 1.5) * (1 + 0.35 * np.sin(xi))
        
        # Radial curvature term with enhanced condition number
        radial_term = np.sum(x**2) * 0.25 * np.exp(-0.1 * np.sum(x**2))
        
        # Combine all terms with proper scaling
        return poly_term + 1.6 * trig_term + 0.45 * exp_term + 0.85 * chaotic_term + 0.35 * radial_term