import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent coupling between dimensions with dynamic weights
        tan_coupling = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.tanh(0.3 * i)
            tan_coupling += weight * np.tanh(x[i]) ** 2
            
        # Polynomial noise modulation with varying exponents
        noise_modulation = 0.0
        for i in range(self.dim):
            exponent = 2 + int(i % 4)
            noise_modulation += 0.3 * np.sin(0.5 * x[i]) * (x[i]**exponent)
            
        # Dynamic ridge structures with sinusoidal modulation
        ridge_terms = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.2 * np.cos(0.4 * i)
            freq = 1.5 + 0.5 * np.sin(0.3 * i)
            ridge_terms += amp * np.exp(-0.1 * (x[i] - freq)**2) * (x[i]**2 + 0.1 * x[i]**4)
            
        # Cross-dimensional hyperbolic coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross_coupling += np.exp(-dist) * np.tanh(x[i] * x[j])
                
        # Chaotic saddle-point components with multiple unstable fixed points
        saddle_terms = 0.0
        for i in range(self.dim):
            saddle_terms += (x[i]**3 - 3.0 * x[i]) * np.sin(0.7 * x[i])
            
        # Adaptive conditioning with dynamic scaling factors based on input magnitude
        conditioning = 0.0
        for i in range(self.dim):
            dyn_scale = 1.0 + 0.4 * np.tanh(x[i] / 2.0)
            conditioning += dyn_scale * x[i]**4
            
        # Asymmetric polynomial components to introduce skewness in the landscape
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += 0.5 * (x[i]**3 + 0.5 * x[i]**5) * np.cos(0.2 * i)
            
        return tan_coupling + noise_modulation + ridge_terms + cross_coupling + saddle_terms + conditioning + asymmetry