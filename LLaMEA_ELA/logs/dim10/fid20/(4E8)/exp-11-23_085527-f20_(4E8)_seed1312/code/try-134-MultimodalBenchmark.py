import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial chaos component with varying exponents
        poly_chaos = np.sum(np.abs(x_scaled)**(2 + np.sin(np.arange(self.dim)) * 3))
        
        # Sinusoidal oscillation with frequency modulation and phase shifts
        sin_osc = 0.0
        for i in range(self.dim):
            freq = (i + 1) * (1.0 + 0.5 * np.sin(i * 0.3))
            phase = 0.2 * np.cos(i * 0.4)
            sin_osc += np.sin(freq * x_scaled[i] + phase) * np.cos(freq * x_scaled[i] + phase)
        
        # Radial basis function with chaotic weight distribution
        rb_fn = 0.0
        for i in range(self.dim):
            weight = 1.0 / (1.0 + 0.1 * i + 0.3 * np.sin(i * 0.7))
            rb_fn += weight * np.exp(-5.0 * np.sum((x_scaled - np.sin(i * 0.5))**2))
        
        # Chaotic interaction terms with logistic map modulation
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Logistic map for chaotic modulation
                log_mod = 4.0 * np.sin(i * 0.2) * np.cos(j * 0.3)
                chaotic_interaction += log_mod * np.sin(10 * x_scaled[i] * x_scaled[j]) * np.cos(5 * x_scaled[i] * x_scaled[j])
        
        # Mixed higher-order polynomial and exponential components
        high_order = 0.0
        for i in range(self.dim):
            high_order += (x_scaled[i]**5 + x_scaled[i]**7) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Combine all components with adaptive scaling
        return 3.0 * poly_chaos + 2.5 * sin_osc + 1.8 * rb_fn + 2.2 * chaotic_interaction + 1.5 * high_order