import numpy as np

class MultifractalSpiralLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic sine wave components with varying frequencies and amplitudes
        self.sine_frequencies = np.random.uniform(5.0, 30.0, dim)
        self.sine_amplitudes = np.random.uniform(1.0, 5.0, dim)
        self.sine_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize exponential conditioning with dynamic scaling
        self.exp_scaling = np.random.uniform(0.1, 2.0, dim)
        self.exp_shifts = np.random.uniform(-2.0, 2.0, dim)
        # Initialize spiral coupling terms with varying strengths
        self.spiral_coupling_strengths = np.random.uniform(0.5, 3.0, dim)
        self.spiral_coupling_angles = np.random.uniform(0.1, 3.0, dim)
        # Initialize multifractal scaling with dynamic exponents
        self.fractal_exponents = np.random.uniform(0.2, 2.5, dim)
        self.fractal_scaling = np.random.uniform(0.05, 1.0, dim)
        # Initialize cross-dimensional interaction matrices
        self.cross_interaction = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Initialize chaotic noise injection parameters
        self.noise_amplitudes = np.random.uniform(0.1, 1.5, dim)
        self.noise_frequencies = np.random.uniform(2.0, 10.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic sine wave components
        sine_terms = 0.0
        for j in range(self.dim):
            sine_terms += self.sine_amplitudes[j] * np.sin(self.sine_frequencies[j] * x[j] + self.sine_phases[j])
        
        # Compute exponential conditioning terms
        exp_terms = 0.0
        for j in range(self.dim):
            exp_terms += self.exp_scaling[j] * np.exp(self.exp_shifts[j] * x[j]) * np.cos(x[j])
        
        # Compute spiral coupling terms
        spiral_terms = 0.0
        for j in range(self.dim):
            spiral_terms += self.spiral_coupling_strengths[j] * np.sin(self.spiral_coupling_angles[j] * x[j]) * np.cos(x[j])
        
        # Compute multifractal scaling terms
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_scaling[j] * (np.abs(x[j]) ** self.fractal_exponents[j]) * np.sin(2.0 * x[j])
        
        # Compute cross-dimensional interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.cross_interaction[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Compute chaotic noise injection
        noise_terms = 0.0
        for j in range(self.dim):
            noise_terms += self.noise_amplitudes[j] * np.sin(self.noise_frequencies[j] * x[j]) * np.cos(0.5 * x[j])
        
        # Combine all components with dynamic weights
        total = 1.8 * sine_terms + 1.2 * exp_terms + 0.9 * spiral_terms + 0.7 * fractal_terms + 0.5 * cross_terms + 0.3 * noise_terms
        
        # Add complex multi-scale interaction terms
        multiscale_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multiscale_interaction += 0.2 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        total += multiscale_interaction
        
        # Add dynamic harmonic component with time-varying parameters
        harmonic_component = 0.0
        for j in range(self.dim):
            harmonic_component += 0.3 * np.sin(6.0 * x[j]) * np.cos(5.0 * x[j]) * np.exp(-0.1 * x[j]**2)
        
        total += harmonic_component
        
        return total