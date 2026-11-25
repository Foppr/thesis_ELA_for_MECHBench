import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for fractal-like behavior and gradient dynamics
        self.fractal_exponents = np.random.uniform(0.3, 0.8, dim)
        self.gradient_magnitudes = np.random.uniform(1.0, 3.0, dim)
        self.basin_depths = np.random.uniform(0.5, 2.0, dim)
        self.adaptation_rates = np.random.uniform(0.1, 0.5, dim)
        self.wave_frequencies = np.random.uniform(2.0, 6.0, dim)
        self.damping_coefficients = np.random.uniform(0.1, 0.4, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Fractal-like potential with self-similar components
        for i in range(self.dim):
            xi = x[i]
            exponent = self.fractal_exponents[i]
            # Multi-scale fractal potential
            fractal_term = np.power(np.abs(xi), exponent) * np.sin(self.wave_frequencies[i] * xi)
            result += fractal_term
            
        # Gradient flow dynamics with adaptive basin structures
        gradient_flow = 0.0
        for i in range(self.dim):
            xi = x[i]
            magnitude = self.gradient_magnitudes[i]
            depth = self.basin_depths[i]
            adaptation = self.adaptation_rates[i]
            
            # Basin-like attraction with dynamic depth
            basin_contribution = -magnitude * np.exp(-depth * np.abs(xi)) * np.sin(adaptation * xi)
            gradient_flow += basin_contribution
            
        result += gradient_flow
        
        # Add cross-dimensional coupling with hybrid harmonic and exponential terms
        coupling_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Hybrid coupling: harmonic + exponential
                harmonic_coupling = np.sin(xi * xj) * np.cos(0.5 * (xi + xj))
                exponential_coupling = np.exp(-0.5 * (xi**2 + xj**2)) * np.sin(xi - xj)
                
                coupling_term += 0.3 * (harmonic_coupling + exponential_coupling)
                
        result += coupling_term
        
        # Add adaptive damping and nonlinear modulation
        damping_modulation = 0.0
        for i in range(self.dim):
            xi = x[i]
            damping = self.damping_coefficients[i]
            
            # Nonlinear damping effect with sinusoidal modulation
            damping_effect = -damping * np.exp(-0.1 * xi**2) * np.sin(3.0 * xi + 0.5 * i)
            damping_modulation += damping_effect
            
        result += damping_modulation
        
        # Add multi-scale oscillatory components for increased complexity
        oscillatory_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple frequency harmonics with varying amplitudes
            harmonic1 = 0.5 * np.sin(2.0 * xi + 0.1 * i)
            harmonic2 = 0.3 * np.sin(5.0 * xi + 0.2 * i)
            harmonic3 = 0.2 * np.sin(8.0 * xi + 0.3 * i)
            
            oscillatory_component += harmonic1 + harmonic2 + harmonic3
            
        result += oscillatory_component
        
        # Add global scaling with fractal dimension modulation
        global_scale = 1.0 + 0.2 * np.sin(0.5 * np.sum(x**2)) * np.cos(0.3 * self.dim)
        result *= global_scale
        
        return result