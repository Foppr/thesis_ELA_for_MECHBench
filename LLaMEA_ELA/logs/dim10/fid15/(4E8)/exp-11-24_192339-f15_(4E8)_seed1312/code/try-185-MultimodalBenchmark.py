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
            freq2 = 1.0 + 0.8 * np.cos(0.4 * x[i])
            freq3 = 0.5 + 0.5 * np.sin(0.6 * x[i])
            chaotic_sine += (np.sin(freq1 * x[i] + np.sin(x[i]**2)) * 
                           np.tanh(x[i]) * 
                           np.cos(freq2 * x[i]) * 
                           np.sin(freq3 * x[i]))
        
        # Dynamic radial basis function with quaternion-inspired interactions
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 1.0 + 0.3 * np.sin(0.5 * (x[i] + x[j]))
                # Quaternion-inspired interaction term
                quat_interaction = np.cos(0.25 * (x[i]**2 + x[j]**2)) * np.sin(0.3 * x[i] * x[j])
                rbf += quat_interaction * np.exp(-0.5 * (dist / width)**2) * np.cos(dist)
        
        # Polynomial interactions with hyperbolic tangent-based cross-dimensional coupling
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperbolic tangent based coupling
                tanh_coupling = np.tanh(x[i] * x[j]) + 0.5 * np.tanh((x[i] - x[j])**2)
                term = (x[i]**2 + x[j]**2) * tanh_coupling * np.exp(-0.1 * (x[i] - x[j])**2)
                poly_coupling += term
        
        # Anti-symmetric coupling terms with fractal-like recursive structure
        antisym_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Anti-symmetric component
                antisym = (x[i] * np.cos(x[j]) - x[j] * np.sin(x[i])) / (1.0 + abs(x[i] - x[j]))
                antisym_term += antisym * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Fractal-like recursive structure with dynamic conditioning
        fractal_cond = 0
        for i in range(self.dim):
            # Recursive-like component with multiple scales
            scale1 = np.sin(3 * x[i]) * np.cos(2 * x[i])
            scale2 = np.tanh(x[i]**3) * np.exp(-0.1 * x[i]**2)
            fractal_cond += (scale1 + scale2) * (1.0 + 0.2 * np.sin(0.5 * x[i]))
        
        # New hyperbolic tangent-based cross-dimensional interaction
        ht_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                ht_interaction += (np.tanh(x[i]) + np.tanh(x[j])) * \
                                np.cos(0.5 * x[i] * x[j]) * \
                                np.exp(-0.02 * (x[i] - x[j])**2)
        
        # Global scaling and skewing factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.1) + 0.2 * np.cos(self.dim * 0.05)
        
        # Combine all components with optimized weights
        return scale_factor * (0.35 * chaotic_sine + 0.25 * rbf + 0.2 * poly_coupling + 
                              0.1 * antisym_term + 0.05 * fractal_cond + 0.05 * ht_interaction)