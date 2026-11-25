import numpy as np

class FractalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Fractal harmonic component with recursive frequency modulation
        fractal_harmonic = 0.0
        for i in range(self.dim):
            freq = 2.0 * (1.0 + np.sin(3.0 * x_scaled[i]) * np.cos(5.0 * x_scaled[i]))
            phase = 2.0 * np.sin(x_scaled[i]**3) + 0.5 * np.cos(x_scaled[i])
            amp = 1.0 + 0.5 * np.sin(7.0 * x_scaled[i])
            fractal_harmonic += amp * np.sin(freq * x_scaled[i] + phase) * np.cos(freq * x_scaled[i] - phase)
        
        # Multi-scale interference pattern with recursive structure
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                # Recursive interference pattern
                interference += (np.sin(10.0 * dist) * np.cos(8.0 * dist) * 
                               np.exp(-dist**2) * (1.0 + 0.3 * np.sin(15.0 * dist)))
        
        # Self-similar ruggedness with scale-invariant features
        ruggedness = 0.0
        for i in range(self.dim):
            # Multiple scales of roughness
            scale1 = np.sin(20.0 * x_scaled[i]) * np.cos(15.0 * x_scaled[i])
            scale2 = np.sin(40.0 * x_scaled[i]) * np.cos(30.0 * x_scaled[i])
            scale3 = np.sin(80.0 * x_scaled[i]) * np.cos(60.0 * x_scaled[i])
            ruggedness += (scale1 + 0.5 * scale2 + 0.25 * scale3) * np.exp(-x_scaled[i]**2)
        
        # Radial fractal component with power-law scaling
        r = np.sqrt(np.sum(x_scaled**2))
        radial_fractal = np.sin(r * 10.0) * np.cos(r * 7.0) * np.exp(-r**3 / 3.0)
        
        # Cross-dimensional coupling with fractal-like interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (np.sin(5.0 * (x_scaled[i] + x_scaled[j])) * 
                           np.cos(4.0 * (x_scaled[i] - x_scaled[j])) *
                           np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2)))
                cross_coupling += coupling
        
        # Combine all components with dynamic weighting
        result = (quadratic * 0.5 + 
                 0.8 * fractal_harmonic + 
                 0.6 * interference + 
                 0.7 * ruggedness + 
                 0.9 * radial_fractal + 
                 0.4 * cross_coupling)
        
        # Add fractal noise with scale-invariant characteristics
        noise = 0.1 * np.random.uniform(-1.0, 1.0) * (1.0 + 0.5 * np.sin(25.0 * r))
        result += noise
        
        return result