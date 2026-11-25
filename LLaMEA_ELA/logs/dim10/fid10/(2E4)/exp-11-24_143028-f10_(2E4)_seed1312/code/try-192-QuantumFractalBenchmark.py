import numpy as np

class QuantumFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.rand(min(10, dim)) * 2.0 + 1.0
        self.mass = np.random.rand(min(10, dim)) * 0.5 + 0.5
        # Fractal Brownian motion parameters
        self.hurst = np.random.rand(min(10, dim)) * 0.4 + 0.3
        # Genetic drift coefficients
        self.drift_coeffs = np.random.randn(min(15, dim)) * 0.3
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator potential
        quantum_term = 0.0
        for i in range(self.dim):
            # Quantum harmonic oscillator energy levels with dimension-dependent frequency
            energy = 0.5 * self.mass[i] * self.omega[i]**2 * x[i]**2
            quantum_term += energy + 0.1 * np.sin(self.omega[i] * x[i]) * np.cos(self.omega[i] * x[i])
        
        # Fractal Brownian motion component with multi-fractal scaling
        fbm_term = 0.0
        for i in range(self.dim):
            # Approximate fractional Brownian motion using spectral synthesis
            freqs = np.linspace(1, 10, min(20, self.dim))
            fbm_sum = 0.0
            for k, freq in enumerate(freqs):
                if k < len(self.hurst):
                    phase = np.random.rand() * 2 * np.pi
                    amp = (1.0 / (freq + 1))**(2 * self.hurst[k])
                    fbm_sum += amp * np.sin(freq * x[i] + phase)
            fbm_term += fbm_sum**2
        
        # Genetic drift and evolutionary pressure components
        genetic_term = 0.0
        for i in range(self.dim):
            # Simulate evolutionary fitness landscape with drift and selection
            drift = self.drift_coeffs[i % len(self.drift_coeffs)] * x[i]
            selection = 0.3 * np.sin(2 * x[i]) * np.cos(3 * x[i])
            genetic_term += drift**2 + selection**3
        
        # Multi-scale interaction terms with fractal coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-coupled interaction between dimensions
                coupling = np.exp(-0.5 * (x[i] - x[j])**2) * \
                          (np.sin(x[i] * x[j]) + 0.2 * np.cos(x[i]**2 + x[j]**2))
                coupling_term += coupling * (1 + 0.1 * np.sin(i * j * 0.5))
        
        # Non-smooth fractal landscape with discontinuous derivatives
        nonsmooth_term = 0.0
        for i in range(self.dim):
            # Create a non-smooth landscape using fractional powers and trigonometric mixing
            nonsmooth_term += (np.abs(x[i])**1.7 + 0.2 * np.sin(5 * x[i]) + 0.1 * np.cos(4 * x[i])) * \
                             (1 + 0.1 * np.sin(0.3 * x[i]) * np.cos(0.2 * x[i]))
        
        # Boundary effects with quantum tunneling-like behavior
        boundary_term = 0.0
        for i in range(self.dim):
            # Simulate quantum-like tunneling at boundaries
            if x[i] < -4.8:
                penalty = 2.0 * np.exp(-0.5 * (x[i] + 4.8)**2) * np.sin(10 * x[i])
                boundary_term += penalty
            elif x[i] > 4.8:
                penalty = 1.5 * np.exp(-0.5 * (x[i] - 4.8)**2) * np.cos(8 * x[i])
                boundary_term += penalty
        
        # Add enhanced complexity through higher-order polynomial interactions and fractal modulation
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Limited interaction to avoid overfitting
                poly_interaction += (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * 0.01
        
        # Combine all components with dimensionally adaptive weights
        result = 0.7 * quantum_term + 0.6 * fbm_term + 0.5 * genetic_term + \
                 0.4 * coupling_term + 0.3 * nonsmooth_term + 0.2 * boundary_term + 0.1 * poly_interaction
        
        return result