import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r_constants = np.linspace(3.5, 4.0, dim)
        self.sigma = 0.02
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-cosine map with frequency modulation
        trig_terms = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_constants[i]
            x_i = x_norm[i]
            trig_terms[i] = r * np.sin(x_i) * np.cos(2 * np.pi * x_i) * np.exp(-0.5 * x_i**2)
        
        # Modified multiquadratic RBF with dynamic centers and adaptive width
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            center = np.sin(i * np.pi / (self.dim + 2))
            width = 0.1 + 0.2 * np.sin(i * np.pi / self.dim)
            rbfs[i] = (x_norm[i] - center)**2 + width * (i + 1)**2
        
        # Adaptive gradient modulation with multiple harmonic components
        grad_mod = np.zeros(self.dim)
        for i in range(self.dim):
            grad_mod[i] = np.exp(-0.2 * (x_norm[i] / (i + 1.0))**2) * (
                np.cos(3 * x_norm[i]) + 0.5 * np.sin(5 * x_norm[i]) + 0.3 * np.cos(7 * x_norm[i])
            )
        
        # Additional nonlinear cross-terms with dynamic coupling coefficients
        cross_terms = np.zeros(self.dim)
        for i in range(self.dim):
            coeff = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            cross_terms[i] = coeff * (x_norm[i]**3) * np.sin(4 * x_norm[(i + 1) % self.dim])
        
        # Combine all terms with improved separability and coupling
        term1 = np.sum(trig_terms**2)
        term2 = np.sum(1.0 / rbfs)
        term3 = np.sum(grad_mod * np.sin(7 * x_norm))
        term4 = np.sum(np.cos(5 * x_norm) * np.exp(-0.15 * x_norm**2))
        term5 = 0.3 * np.sum((x_norm[0] * x_norm[1])**3)
        
        # Enhanced dynamic coupling between dimensions with time-varying coefficients
        coupling = 0.0
        for i in range(self.dim - 1):
            coeff = 0.1 + 0.2 * np.sin(i * np.pi / self.dim)
            coupling += coeff * (x_norm[i] - x_norm[i+1])**3 * np.cos(x_norm[i] * x_norm[i+1])
        
        # Add higher-order polynomial noise with chaotic amplitude modulation
        noise_amp = 0.01 * (1 + np.sin(np.sum(x_norm**2)))
        noise = noise_amp * np.random.random() * np.sum(x_norm**4)
        
        # Add global periodic modulation to increase landscape irregularity
        periodic_mod = 0.2 * np.sin(0.5 * np.sum(x_norm**2))
        
        return term1 + term2 + term3 + term4 + term5 + coupling + noise + periodic_mod