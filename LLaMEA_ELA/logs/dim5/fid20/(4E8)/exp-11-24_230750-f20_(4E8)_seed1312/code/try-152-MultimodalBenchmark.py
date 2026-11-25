import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial polynomial conditioning with chaotic modulation
        r_squared = np.sum(x**2)
        radial_condition = 1.0 + 0.5 * np.sin(r_squared / 8.0) * np.cos(r_squared / 4.0) * np.exp(-r_squared / 50.0)
        
        # Multi-scale composite sinusoidal waves with frequency modulation
        wave = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(i * np.pi / (self.dim + 2)) + 0.8 * np.cos(i * np.pi / (self.dim + 1))
            amp = 1.5 + 0.7 * np.sin(i * np.pi / self.dim) * np.cos(i * np.pi / (self.dim * 2))
            wave += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * np.tanh(x[i])
        
        # Rotational coupling with chaotic phase interference
        rotation = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i])
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                phase = np.sin(dist * (i + j) / 3.0) * np.cos(angle * (i + j) * 0.5)
                rotation += phase * np.sin((i + j) * np.pi / self.dim)
        
        # Multi-scale adaptive noise with chaotic amplitude modulation
        noise_amp = 0.1 * (1.0 + 0.8 * np.sin(r_squared / 3.0)) * (1.0 + 0.3 * np.cos(r_squared / 7.0))
        noise = noise_amp * np.random.randn() * np.exp(-r_squared / 100.0)
        
        # Additional chaotic cross-term interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.cos((x[i] - x[j])**2)
        
        # Combined function value with normalization and chaotic scaling
        result = radial_condition * (wave + rotation + cross_terms) + noise
        
        return result