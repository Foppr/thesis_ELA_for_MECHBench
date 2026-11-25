import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize trigonometric polynomial correlation coefficients with higher variance
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 5))
        # Initialize adaptive radial barrier parameters
        self.barrier_centers = np.random.uniform(-4.5, 4.5, dim)
        self.barrier_widths = np.random.uniform(0.2, 3.0, dim)
        self.barrier_scales = np.random.uniform(0.3, 4.0, dim)
        # Initialize harmonic oscillator parameters with frequency modulation
        self.frequencies = np.random.uniform(0.3, 5.0, dim)
        self.phase_locks = np.random.uniform(-np.pi, np.pi, dim)
        self.amplitude_modulation = np.random.uniform(0.2, 1.0, dim)
        # Add frequency modulation effects
        self.freq_modulation = np.random.uniform(0.1, 0.8, dim)
        # Initialize coupling strengths between dimensions with more complex structure
        self.coupling_strengths = np.random.uniform(0.1, 2.0, (dim, dim))
        # Set diagonal to zero for no self-coupling
        np.fill_diagonal(self.coupling_strengths, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced trigonometric polynomial correlation component
        poly_corr = 0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.poly_coeffs[i, 0] * np.sin(x_i) + 
                        self.poly_coeffs[i, 1] * np.cos(x_i) + 
                        self.poly_coeffs[i, 2] * np.sin(2*x_i) + 
                        self.poly_coeffs[i, 3] * np.cos(2*x_i) +
                        self.poly_coeffs[i, 4] * np.sin(3*x_i))
            poly_corr += poly_term
        
        # Adaptive radial barrier component
        radial_barrier = 0
        for i in range(self.dim):
            center = self.barrier_centers[i]
            width = self.barrier_widths[i]
            scale = self.barrier_scales[i]
            distance = np.abs(x[i] - center)
            # Adaptive Gaussian-like barriers with dynamic width
            adaptive_width = width * (1.0 + 0.5 * np.sin(0.5 * x[i]))
            radial_barrier += scale * np.exp(-0.5 * (distance / adaptive_width)**2)
        
        # Harmonic oscillator component with frequency modulation and amplitude modulation
        harmonic = 0
        for i in range(self.dim):
            freq = self.frequencies[i]
            phase = self.phase_locks[i]
            amp_mod = self.amplitude_modulation[i]
            freq_mod = self.freq_modulation[i]
            # Add sinusoidal oscillation with frequency modulation and amplitude modulation
            harmonic += amp_mod * np.sin(freq * x[i] + phase) + \
                       0.3 * np.sin(3 * freq * x[i] + phase) + \
                       0.1 * np.sin(freq * (1 + freq_mod) * x[i] + phase)
        
        # Cross-dimension coupling with adaptive phase locking
        coupling = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Adaptive coupling strength based on dimension difference
                    diff = np.abs(x[i] - x[j])
                    adaptive_strength = self.coupling_strengths[i, j] * (1.0 + 0.3 * np.sin(diff))
                    coupling += adaptive_strength * np.sin(x[i] - x[j] + self.phase_locks[i] - self.phase_locks[j])
        
        # Add a global scaling factor and noise term for increased complexity
        result = (1.2 * poly_corr + 
                 2.5 * radial_barrier + 
                 1.5 * harmonic + 
                 1.0 * coupling)
        
        return result