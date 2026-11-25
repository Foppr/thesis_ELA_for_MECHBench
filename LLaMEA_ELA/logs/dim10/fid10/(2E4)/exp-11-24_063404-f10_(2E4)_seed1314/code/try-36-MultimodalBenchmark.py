import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced fractal-like radial component with stronger exponential decay and higher frequencies
        r = np.sqrt(np.sum(x_scaled**2))
        fractal_radial = (np.sin(20 * r) * np.exp(-0.5 * r**2) + 
                          0.8 * np.sin(45 * r) * np.exp(-1.2 * r**2) + 
                          0.6 * np.sin(70 * r) * np.exp(-2.5 * r**2) +
                          0.3 * np.sin(100 * r) * np.exp(-4.0 * r**2))
        
        # Enhanced angular component with more complex interacting frequencies
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            # Multiple angular frequencies with chaotic modulation and increased complexity
            for i in range(min(6, self.dim)):
                freq = (i + 1) * 12 + np.sin(i * 3.14159 / 2) * np.cos(i * 3.14159 / 4)
                angular += np.sin(freq * angles) * np.cos(freq * angles) * np.exp(-0.2 * i)
        
        # Enhanced polynomial chaos with higher-order terms and stronger interactions
        poly_chaos = (np.sum(x_scaled**6) + 0.6 * np.sum(x_scaled**5) + 
                     0.4 * np.sum(x_scaled**4) + 0.3 * np.sum(x_scaled**3) + 
                     0.2 * np.sum(x_scaled**2))
        
        # Stronger cross-dimensional interaction terms with more complex coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_scaled[i] * x_scaled[j]) / (1 + 0.8 * np.abs(x_scaled[i] - x_scaled[j]))**2
        
        # Enhanced chaotic perturbation component with higher frequency components
        chaos_perturb = 0.12 * np.sum(np.sin(35 * x_scaled) * np.cos(25 * x_scaled) * 
                                    np.sin(15 * x_scaled))
        
        # Additional harmonic component to increase landscape complexity
        harmonic_component = 0.05 * np.sum(np.sin(50 * x_scaled) * np.cos(30 * x_scaled))
        
        # Combine all components with adjusted weights for increased difficulty
        return (fractal_radial + 0.7 * angular + 0.5 * poly_chaos + 
                0.4 * cross_interaction + 0.2 * chaos_perturb + 
                0.1 * harmonic_component + 0.002 * np.sum(x_scaled**7))