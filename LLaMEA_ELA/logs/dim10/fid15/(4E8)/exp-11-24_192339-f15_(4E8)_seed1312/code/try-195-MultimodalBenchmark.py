import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine wave component with frequency modulation
        chaotic_sine = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[i])
            chaotic_sine += np.sin(freq * x[i] + np.sin(x[i]**2)) * np.tanh(x[i])
        
        # Dynamic radial basis function with quaternion-inspired interactions
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 1.0 + 0.3 * np.sin(0.5 * (x[i] + x[j]))
                # Quaternion-inspired interaction term
                quat_interaction = np.cos(x[i]) * np.sin(x[j]) - np.sin(x[i]) * np.cos(x[j])
                rbf += np.exp(-0.5 * (dist / width)**2) * np.cos(dist) * quat_interaction
        
        # Enhanced polynomial coupling with hyperbolic tangent-based cross-dimensional interactions
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperbolic tangent-based interaction
                tanh_interaction = np.tanh(x[i] * x[j])
                term = (x[i]**2 + x[j]**2) * tanh_interaction * np.exp(-0.1 * (x[i] - x[j])**2)
                poly_coupling += term
        
        # Anti-symmetric coupling terms with fractal-like recursive structure
        antisym_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Anti-symmetric interaction with modified scaling
                asym_interaction = x[i] * np.cos(x[j]) - x[j] * np.cos(x[i])
                antisym_term += asym_interaction * np.exp(-0.03 * (x[i]**2 + x[j]**2))
        
        # Fractal-like noise component with multiple frequency bands and modified amplitude
        noise = 0
        for i in range(self.dim):
            noise += 0.15 * np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.tanh(2 * x[i])
        
        # Global scaling and skewing factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.1) + 0.2 * np.cos(self.dim * 0.05)
        
        # Combine all components with optimized weights for better fitness
        return scale_factor * (0.35 * chaotic_sine + 0.3 * rbf + 0.2 * poly_coupling + 
                              0.1 * antisym_term) + noise