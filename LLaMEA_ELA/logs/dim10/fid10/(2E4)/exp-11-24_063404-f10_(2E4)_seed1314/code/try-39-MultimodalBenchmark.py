import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced fractal-like radial component with sharper transitions
        r = np.sqrt(np.sum(x_scaled**2))
        fractal_radial = (np.sin(15 * r) * np.exp(-0.4 * r**2) + 
                          0.7 * np.sin(30 * r) * np.exp(-0.8 * r**2) + 
                          0.5 * np.sin(50 * r) * np.exp(-2.0 * r**2))
        
        # Modified angular component with higher frequency interactions
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            # Higher frequency angular terms with stronger modulation
            for i in range(min(5, self.dim)):
                freq = (i + 1) * 10 + np.sin(i * 3.14159 / 2.5)
                angular += np.sin(freq * angles) * np.cos(freq * angles) * np.exp(-0.2 * i)
        
        # Enhanced polynomial chaos with higher-order terms
        poly_chaos = np.sum(x_scaled**5) + 0.5 * np.sum(x_scaled**4) + 0.3 * np.sum(x_scaled**3)
        
        # Increased cross-dimensional interaction with stronger coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_scaled[i] * x_scaled[j]) / (1 + 0.7 * np.abs(x_scaled[i] - x_scaled[j]))
        
        # Stronger chaotic perturbation component
        chaos_perturb = 0.1 * np.sum(np.sin(30 * x_scaled) * np.cos(20 * x_scaled))
        
        # Combine all components with adjusted weights for better conditioning
        return (fractal_radial + 0.6 * angular + 0.4 * poly_chaos + 
                0.35 * cross_interaction + 0.2 * chaos_perturb + 0.002 * np.sum(x_scaled**6))