import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic radial component with chaotic modulation
        radius = np.sqrt(np.sum(x**2))
        if radius == 0:
            radius = 1e-10
        log_radial = np.log(radius + 1) * np.sin(3 * radius) * np.cos(5 * radius)
        
        # Asymmetric polynomial potentials with mixed degrees
        asym_poly = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asym_poly += x[i]**6 + 0.5 * x[i]**4 + 0.1 * x[i]**2
            else:
                asym_poly += 0.8 * x[i]**5 + 0.3 * x[i]**3 + 0.05 * x[i]
        asym_poly /= self.dim
        
        # Trigonometric wave interference with variable frequencies and amplitudes
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 2 * (i + 1) + np.sin(i)
            amp = 1.0 / (1.0 + i**0.5)
            wave_interference += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        wave_interference /= self.dim
        
        # Cross-dimensional geometric coupling with exponential decay
        geo_coupling = 0.0
        for i in range(self.dim - 1):
            geo_coupling += np.exp(-0.1 * abs(x[i] - x[i+1])) * np.sin(2 * (x[i] + x[i+1]))
        geo_coupling /= (self.dim - 1)
        
        # Multi-scale chaotic modulation with fractal-like behavior
        fractal_mod = 0.0
        for i in range(self.dim):
            fractal_mod += np.sin(7 * x[i]) * np.cos(13 * x[i]) * np.tan(0.5 * x[i])
        fractal_mod /= self.dim
        
        # Asymmetric Gaussian-like local minima with shifted centers
        gaussian_like = 0.0
        centers = np.linspace(-4, 4, self.dim)
        for i in range(self.dim):
            diff = x[i] - centers[i]
            gaussian_like += np.exp(-0.5 * (diff / (1.0 + 0.1 * abs(diff)))**2)
        gaussian_like /= self.dim
        
        # Combine all components with carefully adjusted weights
        result = (asym_poly * 1.5 + wave_interference * 0.7 + 
                 geo_coupling * 0.9 + fractal_mod * 0.6 + 
                 log_radial * 0.4 + gaussian_like * 0.8)
        
        return float(result)