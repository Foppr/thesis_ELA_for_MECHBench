import numpy as np

class TrigonometricFractalResonance:
    def __init__(self, dim):
        self.dim = dim
        # Initialize trigonometric potential parameters
        self.amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.frequencies = np.random.uniform(0.5, 3.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        self.wave_numbers = np.random.uniform(1.0, 5.0, dim)
        # Initialize resonance parameters
        self.resonance_strengths = np.random.uniform(0.1, 1.5, dim)
        self.resonance_centers = np.random.uniform(-4.0, 4.0, dim)
        self.resonance_widths = np.random.uniform(0.5, 2.0, dim)
        # Initialize fractal parameters
        self.fractal_dims = np.random.uniform(0.1, 1.0, dim)
        self.fractal_amplitudes = np.random.uniform(0.1, 0.5, dim)
        # Initialize interference patterns
        self.interference_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        self.adaptation_rates = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize fitness value
        fitness = 0.0
        
        # Add trigonometric potential wells
        for i in range(self.dim):
            trig_potential = self.amplitudes[i] * np.sin(self.frequencies[i] * x[i] + self.phases[i])**2
            fitness += trig_potential
            
        # Add resonance terms with adaptive centers
        resonance_terms = 0.0
        for i in range(self.dim):
            resonance = self.resonance_strengths[i] * np.exp(-0.5 * ((x[i] - self.resonance_centers[i]) / self.resonance_widths[i])**2)
            resonance_terms += resonance
            
        # Add fractal-like interference patterns
        fractal_terms = 0.0
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, 8):
                fractal_term = self.fractal_amplitudes[i] * np.sin(self.wave_numbers[i] * x[i] * (2**k)) / (k**self.fractal_dims[i])
                fractal_sum += fractal_term
            fractal_terms += fractal_sum
            
        # Add multi-dimensional interference terms
        interference_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference = self.interference_coeffs[i, j] * np.sin(x[i] + x[j])
                interference_terms += interference
                
        # Add adaptive component that modifies the landscape based on previous evaluations
        adaptive_term = 0.0
        # This is a simplified version - in practice this would involve tracking previous evaluations
        for i in range(self.dim):
            adaptive_term += self.adaptation_rates[i] * np.cos(x[i])
            
        # Combine all components with appropriate weights
        total = 0.4 * fitness + 0.3 * resonance_terms + 0.2 * fractal_terms + 0.08 * interference_terms + 0.02 * adaptive_term
        
        return total