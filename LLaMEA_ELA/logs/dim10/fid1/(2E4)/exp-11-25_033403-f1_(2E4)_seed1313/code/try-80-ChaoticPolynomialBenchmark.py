import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 5
        self.sin_frequency = 4.0
        self.radial_factor = 1.5
        self.conditioning_base = 2.0
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree and adaptive conditioning
        poly_term = 0.0
        for i in range(self.dim):
            scale = self.conditioning_base ** (i / self.dim)
            poly_term += scale * (x[i] ** self.poly_degree + 0.4 * x[i] ** 7 + 0.2 * x[i] ** 9)
        
        # Enhanced sinusoidal radial component with multiple harmonic modulations
        r = np.sqrt(np.sum(x**2))
        sin_radial = np.sin(self.sin_frequency * r) * np.cos(0.4 * r) * np.exp(-0.15 * r) * np.sin(0.2 * r)
        radial_term = self.radial_factor * r * sin_radial
        
        # Enhanced cross-dimensional interaction with nonlinear coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(0.5 * x[i] + 0.5 * x[j]) * np.exp(-0.1 * abs(x[i] - x[j]))
                cross_term += interaction * (1 + 0.3 * np.sin(3 * i * j) * np.cos(0.5 * i * j))
        
        # Enhanced harmonic components with frequency modulation and phase shifts
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = self.sin_frequency * (1 + 0.4 * np.sin(i * 0.7))
            phase_shift = 0.3 * np.cos(i * 0.5)
            harmonic_term += np.sin(freq * x[i] + phase_shift) * np.cos(0.9 * freq * x[i] + phase_shift)
        
        # Novel exponential barrier terms with multiple barrier types
        barrier_term = 0.0
        for i in range(self.dim):
            barrier1 = np.exp(1.5 * np.abs(x[i])) * (1 + 0.4 * np.sin(3 * x[i]))
            barrier2 = np.exp(-0.5 * x[i]**2) * (1 + 0.2 * np.cos(2 * x[i]))
            barrier_term += barrier1 + barrier2
            
        # Enhanced chaotic noise component
        noise = 0.08 * np.sum(np.sin(12 * x) ** 2 + 0.5 * np.cos(9 * x) ** 2 + 0.3 * np.sin(6 * x) ** 2)
        
        # Improved global scaling factor with multiple chaotic variations
        global_scale = 1.0 + 0.3 * np.sin(0.4 * r) * np.cos(0.2 * r)
        
        # Combine all terms
        total = poly_term + radial_term + cross_term + harmonic_term + barrier_term + noise
        
        return total * global_scale