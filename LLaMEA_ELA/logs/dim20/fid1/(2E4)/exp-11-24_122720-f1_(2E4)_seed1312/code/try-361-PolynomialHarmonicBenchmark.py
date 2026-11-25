import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize trigonometric polynomial correlation coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        # Initialize multi-scale radial barrier parameters
        self.barrier_centers = np.random.uniform(-4.0, 4.0, dim)
        self.barrier_widths = np.random.uniform(0.3, 2.5, dim)
        self.barrier_scales = np.random.uniform(0.5, 3.0, dim)
        # Initialize harmonic oscillator parameters with phase locking
        self.frequencies = np.random.uniform(0.5, 4.0, dim)
        self.phase_locks = np.random.uniform(-np.pi, np.pi, dim)
        self.amplitude_modulation = np.random.uniform(0.1, 0.8, dim)
        # Initialize coupling strengths between dimensions
        self.coupling_strengths = np.random.uniform(0.2, 1.5, (dim, dim))
        # Set diagonal to zero for no self-coupling
        np.fill_diagonal(self.coupling_strengths, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric polynomial correlation component
        poly_corr = 0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.poly_coeffs[i, 0] * np.sin(x_i) + 
                        self.poly_coeffs[i, 1] * np.cos(x_i) + 
                        self.poly_coeffs[i, 2] * np.sin(2*x_i) + 
                        self.poly_coeffs[i, 3] * np.cos(2*x_i))
            poly_corr += poly_term
        
        # Multi-scale radial barrier component
        radial_barrier = 0
        for i in range(self.dim):
            center = self.barrier_centers[i]
            width = self.barrier_widths[i]
            scale = self.barrier_scales[i]
            distance = np.abs(x[i] - center)
            # Multi-scale Gaussian-like barriers
            radial_barrier += scale * np.exp(-0.5 * (distance / width)**2)
        
        # Harmonic oscillator component with phase locking and amplitude modulation
        harmonic = 0
        for i in range(self.dim):
            freq = self.frequencies[i]
            phase = self.phase_locks[i]
            amp_mod = self.amplitude_modulation[i]
            # Add sinusoidal oscillation with phase locking and amplitude modulation
            harmonic += amp_mod * np.sin(freq * x[i] + phase) + 0.2 * np.sin(3 * freq * x[i] + phase)
        
        # Cross-dimension coupling with phase-locked oscillators
        coupling = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_strengths[i, j] * np.sin(x[i] - x[j] + self.phase_locks[i] - self.phase_locks[j])
        
        # Combine all components with different weights
        result = (1.0 * poly_corr + 
                 2.0 * radial_barrier + 
                 1.2 * harmonic + 
                 0.8 * coupling)
        
        return result