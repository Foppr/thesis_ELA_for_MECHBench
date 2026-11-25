import numpy as np

class ChaoticRadialSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map chaotic parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, size=dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, size=dim)
        # Spectral decomposition components
        self.spectral_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.spectral_amp = np.random.uniform(0.5, 2.5, size=dim)
        # Cross-dimensional coupling coefficients
        self.coupling_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Multi-scale harmonic components
        self.harmonic_orders = np.random.randint(2, 6, size=dim)
        # Adaptive penalty terms
        self.penalty_factors = np.random.uniform(0.5, 2.0, size=dim)
        # Fractal-like scaling exponents
        self.fractal_exponents = np.random.uniform(1.2, 3.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component
        logistic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Iterate logistic map multiple times for chaos
            for _ in range(5):
                xi = self.logistic_r[i] * xi * (1 - xi)
            logistic_component += xi
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_val = 0.0
            for j in range(self.dim):
                dist = np.linalg.norm(x - self.rbf_centers[i, :])
                rbf_val += np.exp(-0.5 * (dist / self.rbf_widths[i])**2)
            rbf_component += rbf_val
            
        # Spectral decomposition component
        spectral_component = 0.0
        for i in range(self.dim):
            # Fourier-like spectral terms
            spec_val = self.spectral_amp[i] * np.sin(self.spectral_freq[i] * x[i])
            spectral_component += spec_val
            
        # Cross-dimensional coupling
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_coeffs[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Multi-scale harmonic interaction
        harmonic_component = 0.0
        for i in range(self.dim):
            harm_val = 0.0
            for k in range(1, self.harmonic_orders[i] + 1):
                harm_val += np.sin(k * x[i]) / k
            harmonic_component += harm_val
            
        # Fractal-like scaling component
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_val = x[i]**self.fractal_exponents[i]
            fractal_component += fractal_val
            
        # Adaptive penalty term
        penalty_component = 0.0
        for i in range(self.dim):
            penalty_component += self.penalty_factors[i] * (x[i] - np.sin(x[i]))**2
            
        # Combine all components with different weights
        return (1.2 * logistic_component + 
                1.0 * rbf_component + 
                0.9 * spectral_component + 
                0.8 * coupling_component + 
                0.7 * harmonic_component + 
                0.6 * fractal_component + 
                0.5 * penalty_component)