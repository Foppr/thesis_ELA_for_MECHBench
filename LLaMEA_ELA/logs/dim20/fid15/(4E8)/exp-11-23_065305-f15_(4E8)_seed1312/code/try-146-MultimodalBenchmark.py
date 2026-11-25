import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic radial component with nested sinusoidal modulation
        radius = np.sqrt(np.sum(x**2))
        if radius == 0:
            radius = 1e-10
        radial_component = (np.log(radius + 1) * 
                          np.sin(2 * radius) * 
                          np.cos(3 * radius) * 
                          np.exp(-0.2 * radius) * 
                          np.sin(0.3 * radius**2))
        
        # Asymmetric polynomial potentials with chaotic coefficients and mixed degrees
        asym_poly = 0.0
        for i in range(self.dim):
            coeff1 = 1.2 + 0.3 * np.sin(i * 1.7)
            coeff2 = 0.9 + 0.1 * np.cos(i * 2.3)
            if x[i] >= 0:
                asym_poly += coeff1 * x[i]**5 + coeff2 * x[i]**3 + 0.15 * x[i]**2
            else:
                asym_poly += 0.7 * x[i]**4 + 0.2 * x[i]**2 + 0.08 * x[i]
        asym_poly /= self.dim
        
        # Enhanced trigonometric wave interference with chaotic frequencies and phase shifts
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 3 * (i + 1) + 0.5 * np.sin(i * 0.8) + 0.2 * np.cos(2 * i)
            amp = 1.2 / (1.0 + i**0.6 + 0.15 * np.sin(2 * i))
            phase_shift = 0.15 * np.sin(i * 0.7 + 0.3 * np.cos(i))  # Modified phase shift
            wave_interference += amp * np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] * 0.8 + phase_shift)
        wave_interference /= self.dim
        
        # Cross-dimensional coupling with chaotic exponential decay and modified interaction terms
        geo_coupling = 0.0
        for i in range(self.dim - 1):
            decay_factor = np.exp(-0.2 * abs(x[i] - x[i+1])) * (1 + 0.3 * np.sin(i * 1.3))  # Modified decay rate
            geo_coupling += decay_factor * np.sin(3 * (x[i] + x[i+1]))
        geo_coupling /= (self.dim - 1)
        
        # Multi-scale chaotic modulation with fractal-like behavior and nested sinusoidal components
        fractal_mod = 0.0
        for i in range(self.dim):
            fractal_mod += (np.sin(5 * x[i]) * np.cos(9 * x[i]) * 
                           np.tan(0.4 * x[i]) * 
                           np.exp(-0.08 * abs(x[i])) * 
                           np.sin(0.2 * x[i]**2))
        fractal_mod /= self.dim
        
        # Asymmetric Gaussian-like local minima with shifted centers and chaotic variance
        gaussian_like = 0.0
        centers = np.linspace(-4, 4, self.dim)
        for i in range(self.dim):
            diff = x[i] - centers[i]
            variance = 1.2 + 0.3 * np.sin(i * 1.5)
            gaussian_like += np.exp(-0.5 * (diff / (variance + 0.15 * abs(diff)))**2)
        gaussian_like /= self.dim
        
        # Additional chaotic radial basis function component with modified parameters
        rbf_component = 0.0
        for i in range(self.dim):
            center = -3.5 + 7.0 * i / (self.dim - 1) if self.dim > 1 else 0.0
            rbf_component += np.exp(-0.5 * ((x[i] - center) / (1.2 + 0.15 * np.sin(i)))**2) * np.sin(2.5 * x[i])
        rbf_component /= self.dim
        
        # Novel asymmetric fractal potential component with chaotic interaction terms
        fractal_potential = 0.0
        for i in range(self.dim):
            base_term = np.sin(4 * x[i]) * np.cos(7 * x[i])
            interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction += np.sin(2 * (x[i] - x[j])) * np.cos(3 * (x[i] + x[j]))
            fractal_potential += base_term * (1 + 0.2 * np.sin(i * 1.8)) * interaction
        fractal_potential /= self.dim
        
        # Combine all components with adjusted weights for improved fitness
        result = (asym_poly * 2.0 + wave_interference * 1.1 + 
                 geo_coupling * 1.4 + fractal_mod * 0.8 + 
                 radial_component * 0.6 + gaussian_like * 1.2 + 
                 rbf_component * 0.7 + fractal_potential * 1.5)
        
        return float(result)