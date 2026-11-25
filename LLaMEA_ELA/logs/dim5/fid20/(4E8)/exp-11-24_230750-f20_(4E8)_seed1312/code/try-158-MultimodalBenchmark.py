import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic structure with hyperbolic tangent coupling
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperbolic tangent coupling between dimensions
                coupling = np.tanh(x[i] * x[j])
                # Chaotic interaction with sine and cosine
                chaotic += np.sin(x[i]**2 + x[j]**2) * np.cos(coupling)
        
        # Modified trigonometric components with dynamic frequencies
        trig = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * np.pi / (self.dim + 1))
            amp = 1.5 + 0.5 * np.cos(i * np.pi / self.dim)
            # Enhanced sinusoidal with cubic term
            trig += amp * np.sin(freq * x[i] + 0.5 * x[i]**3) * np.cos(freq * x[i]**2)
        
        # Augmented polynomial cross-terms with adaptive exponents
        poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive exponent based on dimension indices
                exp = 2.0 + 0.5 * np.sin((i + j) * np.pi / (self.dim + 1))
                poly += (x[i]**exp) * (x[j]**(exp + 0.5))
        
        # Radial polynomial conditioning with chaotic modulation
        r_squared = np.sum(x**2)
        radial_condition = 1.0 + 0.4 * np.sin(r_squared / 8.0) * np.cos(r_squared / 4.0) * np.tanh(r_squared / 25.0)
        
        # Novel noise mechanism with position-dependent amplitude
        noise_amp = 0.03 * (1.0 + 0.3 * np.sin(r_squared / 6.0))
        noise = noise_amp * np.random.randn()
        
        # Combine all components with proper scaling
        result = radial_condition * (trig + chaotic + poly) + noise
        
        return result