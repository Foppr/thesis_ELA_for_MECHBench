import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced fractal-like radial component with sharper transitions and modified decay
        r = np.sqrt(np.sum(x_scaled**2))
        fractal_radial = (np.sin(18 * r) * np.exp(-0.3 * r**2) + 
                          0.8 * np.sin(35 * r) * np.exp(-0.6 * r**2) + 
                          0.6 * np.sin(60 * r) * np.exp(-1.5 * r**2))
        
        # Modified angular component with higher frequency interactions and stronger modulation
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            # Higher frequency angular terms with stronger modulation
            for i in range(min(6, self.dim)):
                freq = (i + 1) * 12 + np.sin(i * 3.14159 / 2.0)
                angular += np.sin(freq * angles) * np.cos(freq * angles) * np.exp(-0.15 * i)
        
        # Enhanced polynomial chaos with higher-order terms and modified coefficients
        poly_chaos = np.sum(x_scaled**5) + 0.6 * np.sum(x_scaled**4) + 0.4 * np.sum(x_scaled**3)
        
        # Increased cross-dimensional interaction with stronger coupling and additional nonlinear terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_scaled[i] * x_scaled[j]) / (1 + 0.8 * np.abs(x_scaled[i] - x_scaled[j])) + 0.1 * np.sin(5 * x_scaled[i]) * np.cos(5 * x_scaled[j])
        
        # Stronger chaotic perturbation component with modified frequency
        chaos_perturb = 0.15 * np.sum(np.sin(35 * x_scaled) * np.cos(25 * x_scaled))
        
        # Additional sinusoidal coupling term to increase landscape complexity
        coupling_term = 0.05 * np.sum(np.sin(20 * x_scaled) * np.exp(-0.5 * r**2))
        
        # Combine all components with adjusted weights for better conditioning
        return (fractal_radial + 0.7 * angular + 0.5 * poly_chaos + 
                0.4 * cross_interaction + 0.25 * chaos_perturb + 0.003 * np.sum(x_scaled**6) + coupling_term)