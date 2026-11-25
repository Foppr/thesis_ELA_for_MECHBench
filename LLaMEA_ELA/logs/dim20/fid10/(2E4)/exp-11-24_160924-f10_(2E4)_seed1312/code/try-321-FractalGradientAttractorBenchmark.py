import numpy as np

class FractalGradientAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize fractal parameters
        self.fractal_dimensions = np.random.uniform(1.1, 2.5, dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.gradient_weights = np.random.uniform(0.3, 1.7, dim)
        self.resonance_frequencies = np.random.uniform(2.0, 8.0, dim)
        self.attractor_strengths = np.random.uniform(1.0, 4.0, dim)
        self.noise_intensities = np.random.uniform(0.05, 0.3, dim)
        self.hill_climbing_factors = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add fractal-like ridge components with self-similar structures
        for i in range(self.dim):
            xi = x[i]
            fdim = self.fractal_dimensions[i]
            amp = self.fractal_amplitudes[i]
            
            # Fractal ridge with multiple scales
            fractal_term = amp * np.sin(xi) * np.cos(xi)
            fractal_term += 0.5 * amp * np.sin(2 * xi) * np.cos(2 * xi)
            fractal_term += 0.3 * amp * np.sin(4 * xi) * np.cos(4 * xi)
            result += fractal_term
            
        # Add hybrid gradient-flow structures
        for i in range(self.dim):
            xi = x[i]
            weight = self.gradient_weights[i]
            
            # Hybrid quadratic and exponential gradient components
            grad_flow = weight * (xi**2 + 0.5 * np.exp(-0.1 * xi**2))
            result += grad_flow
            
        # Add stochastic resonance with multiple frequency components
        for i in range(self.dim):
            xi = x[i]
            freq = self.resonance_frequencies[i]
            noise_int = self.noise_intensities[i]
            
            # Stochastic resonance term with multiple harmonics
            resonance = noise_int * np.sin(freq * xi) * np.cos(freq * xi)
            resonance += 0.3 * noise_int * np.sin(2 * freq * xi) * np.cos(2 * freq * xi)
            result += resonance
            
        # Add attractor basin components with varying strengths
        for i in range(self.dim):
            xi = x[i]
            strength = self.attractor_strengths[i]
            
            # Multi-scale attractor basins
            basin_term = strength * (np.exp(-0.5 * (xi - 1)**2) + np.exp(-0.5 * (xi + 1)**2))
            result += basin_term
            
        # Add hierarchical hill-climbing mechanisms
        for i in range(self.dim):
            xi = x[i]
            factor = self.hill_climbing_factors[i]
            
            # Hierarchical climbing terms with different scales
            climb_term = factor * (xi**4 - 6*xi**2 + 8)
            result += climb_term
            
        # Add cross-dimensional coupling with fractal scaling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Fractal coupling with dimension-dependent scaling
                scale_factor = (self.fractal_dimensions[i] + self.fractal_dimensions[j]) / 2.0
                coupling = 0.3 * np.sin(scale_factor * (xi + xj)) * np.cos(scale_factor * (xi - xj))
                result += coupling
                
        # Add global scaling with fractal dimension modulation
        global_scale = 1.0 + 0.5 * np.sin(np.sum(self.fractal_dimensions) / self.dim)
        result *= global_scale
        
        # Add multi-scale harmonic structure
        harmonic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            harmonic_sum += (np.sin(3 * xi) + 0.5 * np.sin(6 * xi) + 0.2 * np.sin(9 * xi)) * (xi**2 - 4)
        result += 0.4 * harmonic_sum
        
        # Add chaotic-like perturbations with deterministic fractal patterns
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_perturbation += np.sin(15.0 * xi) * np.cos(10.0 * xi) * (1 + 0.2 * np.sin(5.0 * xi))
        result += 0.15 * chaotic_perturbation
        
        return result