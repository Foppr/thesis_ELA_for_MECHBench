import numpy as np

class TrigonometricChaosEpistasisBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic sine-wave parameters for each dimension
        self.sin_freqs = np.random.uniform(2.0, 8.0, dim)
        self.sin_ampls = np.random.uniform(0.5, 2.0, dim)
        self.sin_phases = np.random.uniform(0.0, 2.0 * np.pi, dim)
        # Genetic algorithm inspired epistasis coefficients
        self.epistasis_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Fractal coupling parameters between dimensions
        self.fractal_exp = np.random.uniform(0.3, 0.9, dim)
        self.fractal_scale = np.random.uniform(0.1, 0.5, dim)
        # Multi-scale chaotic components
        self.chaos_freqs = np.random.uniform(1.0, 10.0, 5)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Trigonometric chaos component with phase shifts and varying frequencies
        for i in range(self.dim):
            trig_sum = 0.0
            for j in range(3):
                trig_sum += self.sin_ampls[i] * np.sin(self.sin_freqs[i] * x_norm[i] + self.sin_phases[i])
            f_val += 0.25 * (trig_sum**2 + 0.1 * trig_sum**4)
        
        # Epistasis interaction terms inspired by genetic algorithms
        for i in range(self.dim):
            epistasis_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    epistasis_sum += self.epistasis_coeffs[i, j] * np.sin(x_norm[i] * x_norm[j])
            f_val += 0.2 * (epistasis_sum**2 + 0.05 * epistasis_sum**3)
        
        # Fractal-based coupling between dimensions
        for i in range(self.dim):
            fractal_term = 0.0
            for j in range(self.dim):
                if i != j:
                    fractal_term += self.fractal_scale[i] * np.abs(x_norm[i] - x_norm[j])**(self.fractal_exp[i])
            f_val += 0.15 * fractal_term
        
        # Multi-scale chaotic components with different frequencies
        for k in range(5):
            chaos_sum = 0.0
            for i in range(self.dim):
                chaos_sum += np.sin(self.chaos_freqs[k] * x_norm[i])
            f_val += 0.1 * (np.abs(chaos_sum)**1.8 + 0.03 * np.abs(chaos_sum)**2.5)
        
        # Add basin boundary irregularity with polynomial perturbations
        poly_pert = 0.0
        for i in range(self.dim):
            poly_pert += (x_norm[i]**3 - 0.5 * x_norm[i]**2 + 0.1 * x_norm[i])
        f_val += 0.1 * poly_pert**2
        
        # Add noise-like perturbations with non-uniform scaling
        noise_pert = 0.05 * np.sum(
            np.sin(3.0 * x_norm) * np.cos(2.0 * x_norm) +
            np.tan(1.5 * x_norm) * np.exp(-0.5 * x_norm**2) +
            0.2 * np.sin(4.0 * x_norm)**3
        )
        f_val += noise_pert
        
        return f_val