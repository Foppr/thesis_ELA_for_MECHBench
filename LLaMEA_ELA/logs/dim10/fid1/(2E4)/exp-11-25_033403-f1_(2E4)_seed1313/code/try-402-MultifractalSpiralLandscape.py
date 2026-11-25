import numpy as np

class MultifractalSpiralLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logarithmic spiral components with varying radii and angles
        self.spiral_radii = np.random.uniform(0.5, 3.0, dim)
        self.spiral_angles = np.random.uniform(0.1, 2.0, dim)
        self.spiral_coefficients = np.random.uniform(-2.0, 2.0, dim)
        # Initialize sinusoidal wave components with dynamic frequencies and amplitudes
        self.wave_frequencies = np.random.uniform(1.0, 15.0, dim)
        self.wave_amplitudes = np.random.uniform(0.5, 4.0, dim)
        self.wave_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize multifractal scaling parameters
        self.fractal_scaling = np.random.uniform(0.1, 1.5, dim)
        self.fractal_exponents = np.random.uniform(0.3, 1.8, dim)
        # Initialize adaptive conditioning with dynamic weights
        self.conditioning_weights = np.random.uniform(0.2, 3.0, dim)
        self.conditioning_shifts = np.random.uniform(-1.0, 1.0, dim)
        # Initialize cross-dimensional coupling terms
        self.cross_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Initialize logarithmic interaction terms
        self.log_coefficients = np.random.uniform(0.1, 2.0, dim)
        # Initialize hyperbolic tangent components
        self.tanh_coefficients = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute logarithmic spiral components
        spiral_terms = 0.0
        for j in range(self.dim):
            radius = self.spiral_radii[j] * np.exp(self.spiral_angles[j] * x[j])
            spiral_terms += self.spiral_coefficients[j] * np.sin(radius) * np.cos(radius)
        
        # Compute sinusoidal wave components
        wave_terms = 0.0
        for j in range(self.dim):
            wave_terms += self.wave_amplitudes[j] * np.sin(self.wave_frequencies[j] * x[j] + self.wave_phases[j])
        
        # Compute multifractal scaling terms
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_scaling[j] * (np.abs(x[j]) ** self.fractal_exponents[j]) * np.sin(x[j])
        
        # Compute adaptive conditioning
        conditioning_terms = 0.0
        for j in range(self.dim):
            conditioning_terms += self.conditioning_weights[j] * np.log(1.0 + np.abs(x[j])) * np.cos(self.conditioning_shifts[j] * x[j])
        
        # Compute cross-dimensional coupling terms
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.cross_coupling[i, j] * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Compute logarithmic interaction terms
        log_terms = 0.0
        for j in range(self.dim):
            log_terms += self.log_coefficients[j] * np.log(1.0 + np.abs(x[j])) * np.sin(x[j])
        
        # Compute hyperbolic tangent components
        tanh_terms = 0.0
        for j in range(self.dim):
            tanh_terms += self.tanh_coefficients[j] * np.tanh(x[j]) * np.cos(0.5 * x[j])
        
        # Combine all components with appropriate weights
        total = 1.2 * spiral_terms + 1.5 * wave_terms + 0.8 * fractal_terms + 0.6 * conditioning_terms + 0.4 * cross_terms + 0.3 * log_terms + 0.2 * tanh_terms
        
        # Add a complex interaction term: multi-scale multifractal coupling
        multifractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multifractal_coupling += 0.15 * np.sin(3.0 * (x[i] + x[j])) * np.cos(2.0 * (x[i] - x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        total += multifractal_coupling
        
        # Add a dynamic harmonic component with time-varying parameters
        harmonic_component = 0.0
        for j in range(self.dim):
            harmonic_component += 0.25 * np.sin(4.0 * x[j]) * np.cos(3.0 * x[j]) * np.exp(-0.05 * x[j]**2)
        
        total += harmonic_component
        
        return total