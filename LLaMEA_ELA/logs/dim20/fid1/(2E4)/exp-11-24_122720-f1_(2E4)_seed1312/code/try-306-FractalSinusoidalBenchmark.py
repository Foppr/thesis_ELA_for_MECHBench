import numpy as np

class FractalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters for sinusoidal components
        self.fractal_freq = [np.random.uniform(1.0, 3.0) for _ in range(dim)]
        self.fractal_amp = [np.random.uniform(0.5, 2.0) for _ in range(dim)]
        self.symmetry_order = np.random.randint(3, 8)
        self.coupling_strength = np.random.uniform(0.1, 0.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal scaling
        radius = np.sqrt(np.sum(x**2))
        radial_fractal = 1.0 + 0.3 * np.sin(radius * np.pi)
        
        # Sinusoidal components with fractal frequencies and amplitudes
        sinusoidal = 0
        for i in range(self.dim):
            freq = self.fractal_freq[i]
            amp = self.fractal_amp[i]
            sinusoidal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Radial sinusoidal component with symmetry
        radial_sine = 0
        for i in range(self.dim):
            radial_sine += np.sin(self.symmetry_order * np.arctan2(x[i], radius))
            
        # Cross-dimensional coupling with fractal weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                coupling += self.coupling_strength * np.sin(dist) * np.cos(dist)
                
        # Fractal basin component with multiple scales
        basin = 0
        for i in range(self.dim):
            scale1 = np.abs(x[i]) ** (1.5 + 0.5 * np.sin(i))
            scale2 = np.abs(x[i]) ** (2.0 + 0.3 * np.cos(i))
            basin += scale1 + scale2
            
        # Add chaotic noise component
        noise = np.random.normal(0, 0.1) * np.sum(np.sin(x))
        
        # Combine all components with adaptive weights
        result = 0.8 * sinusoidal + 0.6 * radial_sine + 0.4 * coupling + 0.3 * basin + 0.2 * noise
        
        return result