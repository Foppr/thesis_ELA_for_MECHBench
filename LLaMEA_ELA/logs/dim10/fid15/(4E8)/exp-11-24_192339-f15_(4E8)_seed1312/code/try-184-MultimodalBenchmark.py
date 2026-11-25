import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine wave component with multi-frequency modulation
        chaotic_sine = 0
        for i in range(self.dim):
            freq1 = 2.0 + 1.5 * np.sin(0.3 * x[i])
            freq2 = 1.0 + 0.8 * np.cos(0.4 * x[i] + 0.5)
            freq3 = 0.5 + 0.3 * np.sin(0.7 * x[i]**2)
            chaotic_sine += np.sin(freq1 * x[i] + np.sin(freq2 * x[i])) * np.tanh(freq3 * x[i])
        
        # Dynamic radial basis function with quaternion-inspired interactions
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 1.0 + 0.4 * np.sin(0.5 * (x[i] + x[j]))
                # Quaternion-inspired coupling
                coupling = np.cos(0.3 * x[i]) * np.sin(0.3 * x[j]) + np.sin(0.3 * x[i]) * np.cos(0.3 * x[j])
                rbf += coupling * np.exp(-0.5 * (dist / width)**2) * np.cos(dist)
        
        # Polynomial interactions with hyperbolic tangent-based cross-dimensional coupling
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperbolic tangent-based coupling
                tan_coupling = np.tanh(x[i] * x[j]) + 0.5 * np.tanh((x[i] + x[j])**2)
                term = (x[i]**2 + x[j]**2) * tan_coupling * np.exp(-0.1 * (x[i] - x[j])**2)
                poly_coupling += term
        
        # Asymmetric skewing mechanism with fractal-like recursive structure
        skew_term = 0
        for i in range(self.dim):
            # Recursive asymmetric skewing
            skew_factor = 1.0 + 0.3 * np.sin(0.5 * x[i]) + 0.2 * np.cos(0.7 * x[i]**2)
            skew_term += np.tanh(x[i]) * skew_factor * np.exp(-0.05 * x[i]**2)
        
        # Dynamic conditioning with polynomial scaling and anti-symmetric coupling
        cond = 0
        for i in range(self.dim):
            cond += (x[i]**4 + 0.5 * x[i]**3) * np.tanh(x[i]) * (1.0 + 0.2 * np.cos(0.3 * x[i]))
        
        # Fractal-like noise component with anti-symmetric coupling terms
        noise = 0
        for i in range(self.dim):
            # Anti-symmetric noise component
            noise += 0.1 * (np.sin(5 * x[i]) * np.cos(7 * x[i]) - 
                           np.cos(5 * x[i]) * np.sin(7 * x[i])) * np.tanh(2 * x[i])
        
        # New fractal-like recursive structure with anti-symmetric coupling terms
        fractal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Anti-symmetric coupling
                asym_coupling = (x[i] - x[j]) * np.tanh(x[i] + x[j])
                fractal += asym_coupling * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Global scaling and skewing factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.1) + 0.2 * np.cos(self.dim * 0.05)
        
        # Combine all components with optimized weights for better discrimination
        return scale_factor * (0.35 * chaotic_sine + 0.3 * rbf + 0.2 * poly_coupling + 
                              0.1 * skew_term + 0.05 * cond + 0.05 * fractal) + noise