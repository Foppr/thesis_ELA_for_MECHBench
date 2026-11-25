import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for fractal-like behavior and gradient dynamics
        self.fractal_exponents = np.random.uniform(0.25, 0.85, dim)
        self.gradient_magnitudes = np.random.uniform(1.2, 2.8, dim)
        self.basin_depths = np.random.uniform(0.6, 1.8, dim)
        self.adaptation_rates = np.random.uniform(0.15, 0.45, dim)
        self.wave_frequencies = np.random.uniform(1.5, 6.5, dim)
        self.damping_coefficients = np.random.uniform(0.05, 0.45, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Fractal-like potential with self-similar components
        for i in range(self.dim):
            xi = x[i]
            exponent = self.fractal_exponents[i]
            # Multi-scale fractal potential with modified sinusoidal modulation
            fractal_term = np.power(np.abs(xi), exponent) * np.sin(self.wave_frequencies[i] * xi + 0.2 * i)
            result += fractal_term
            
        # Gradient flow dynamics with adaptive basin structures
        gradient_flow = 0.0
        for i in range(self.dim):
            xi = x[i]
            magnitude = self.gradient_magnitudes[i]
            depth = self.basin_depths[i]
            adaptation = self.adaptation_rates[i]
            
            # Basin-like attraction with dynamic depth and modified exponential decay
            basin_contribution = -magnitude * np.exp(-depth * np.abs(xi) + 0.1 * xi**2) * np.sin(adaptation * xi + 0.3 * i)
            gradient_flow += basin_contribution
            
        result += gradient_flow
        
        # Add cross-dimensional coupling with hybrid harmonic and exponential terms
        coupling_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Hybrid coupling: harmonic + exponential with modified coefficients
                harmonic_coupling = 0.4 * np.sin(xi * xj) * np.cos(0.6 * (xi + xj))
                exponential_coupling = 0.2 * np.exp(-0.3 * (xi**2 + xj**2)) * np.sin(xi - xj + 0.1 * (i+j))
                
                coupling_term += harmonic_coupling + exponential_coupling
                
        result += coupling_term
        
        # Add adaptive damping and nonlinear modulation
        damping_modulation = 0.0
        for i in range(self.dim):
            xi = x[i]
            damping = self.damping_coefficients[i]
            
            # Nonlinear damping effect with sinusoidal modulation and additional phase shift
            damping_effect = -damping * np.exp(-0.15 * xi**2) * np.sin(3.5 * xi + 0.6 * i)
            damping_modulation += damping_effect
            
        result += damping_modulation
        
        # Add multi-scale oscillatory components for increased complexity
        oscillatory_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple frequency harmonics with varying amplitudes and phase shifts
            harmonic1 = 0.6 * np.sin(2.5 * xi + 0.15 * i)
            harmonic2 = 0.35 * np.sin(4.5 * xi + 0.25 * i)
            harmonic3 = 0.25 * np.sin(7.5 * xi + 0.35 * i)
            
            oscillatory_component += harmonic1 + harmonic2 + harmonic3
            
        result += oscillatory_component
        
        # Add global scaling with fractal dimension modulation
        global_scale = 1.0 + 0.25 * np.sin(0.4 * np.sum(x**2)) * np.cos(0.35 * self.dim)
        result *= global_scale
        
        return result