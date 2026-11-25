import numpy as np

class FractalGradientAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension with fractal and gradient properties
        self.fractal_dimensions = np.random.uniform(1.2, 2.8, dim)
        self.gradient_magnitudes = np.random.uniform(0.3, 3.5, dim)
        self.attractor_positions = np.random.uniform(-4.5, 4.5, dim)
        self.attractor_strengths = np.random.uniform(0.8, 4.5, dim)
        self.resonance_frequencies = np.random.uniform(0.3, 3.5, dim)
        self.fractal_amplitudes = np.random.uniform(0.3, 3.0, dim)
        self.hill_climbing_rates = np.random.uniform(0.05, 0.95, dim)
        self.stochastic_noise_levels = np.random.uniform(0.005, 0.35, dim)
        self.basin_widths = np.random.uniform(0.3, 2.5, dim)
        self.coupling_strengths = np.random.uniform(0.1, 1.2, (dim, dim))
        self.multiscale_factors = np.random.uniform(0.05, 2.0, dim)
        self.spectral_peaks = np.random.uniform(0.8, 6.0, dim)
        self.quantum_phases = np.random.uniform(0, 2*np.pi, dim)
        self.tunnel_depths = np.random.uniform(0.5, 3.0, dim)
        self.interference_strengths = np.random.uniform(0.1, 2.0, dim)
        self.adaptivity_rates = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Fractal gradient components with self-similar structure
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dimensions[i]
            grad_mag = self.gradient_magnitudes[i]
            
            # Multi-scale fractal gradient with power-law scaling and quantum interference
            fractal_gradient = grad_mag * np.sin(xi) * np.cos(xi)
            fractal_gradient += 0.5 * np.sin(2 * xi) * np.cos(2 * xi)
            fractal_gradient += 0.3 * np.sin(4 * xi) * np.cos(4 * xi)
            
            # Quantum-like interference term
            quantum_term = self.interference_strengths[i] * np.sin(xi + self.quantum_phases[i]) * np.cos(xi - self.quantum_phases[i])
            fractal_gradient += quantum_term
            
            # Power-law scaling with fractal dimension
            result += fractal_gradient * (np.abs(xi)**fractal_dim)
            
        # Hybrid attractor landscape with resonance phenomena and tunneling
        for i in range(self.dim):
            xi = x[i]
            pos = self.attractor_positions[i]
            strength = self.attractor_strengths[i]
            freq = self.resonance_frequencies[i]
            
            # Stochastic resonance-like attraction with fractal basin and quantum tunneling
            distance = np.abs(xi - pos)
            basin_width = self.basin_widths[i] * (1.0 + 0.3 * np.sin(0.5 * xi))
            
            # Tunneling effect with adaptive depth
            tunnel_depth = self.tunnel_depths[i] * (1.0 + 0.2 * np.cos(xi))
            tunnel_factor = np.exp(-distance**2 / (2 * basin_width**2)) * (1.0 + tunnel_depth * np.sin(3 * xi))
            
            # Multi-scale basin attraction with power-law decay
            attractor_term = strength * tunnel_factor
            result += attractor_term
            
        # Multiscale fractal components with hybrid harmonic structure and quantum effects
        for i in range(self.dim):
            xi = x[i]
            amp = self.fractal_amplitudes[i]
            scale_factor = self.multiscale_factors[i]
            
            # Multi-scale fractal harmonic with spectral peaks and quantum phases
            fractal_component = amp * np.sin(scale_factor * xi) * np.cos(scale_factor * xi)
            fractal_component += 0.5 * np.sin(2 * scale_factor * xi) * np.cos(2 * scale_factor * xi)
            fractal_component += 0.3 * np.sin(3 * scale_factor * xi) * np.cos(3 * scale_factor * xi)
            
            # Quantum phase modulation
            quantum_mod = self.quantum_phases[i] * np.cos(xi)
            fractal_component += 0.4 * np.sin(xi + quantum_mod) * np.cos(xi - quantum_mod)
            
            # Spectral peak modulation
            spectral_mod = self.spectral_peaks[i] * np.sin(xi)
            result += fractal_component * (1.0 + 0.2 * spectral_mod)
            
        # Cross-dimensional coupling with hybrid fractal interaction and quantum interference
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling_strength = self.coupling_strengths[i][j]
                
                # Fractal-like cross-dimension coupling with power-law interaction and quantum interference
                coupling_term = coupling_strength * np.sin(xi + xj) * np.cos(xi - xj)
                coupling_term += 0.4 * np.sin(2 * (xi + xj)) * np.cos(2 * (xi - xj))
                
                # Quantum interference between dimensions
                quantum_coupling = self.interference_strengths[i] * np.sin(xi + xj + self.quantum_phases[i]) * np.cos(xi - xj + self.quantum_phases[j])
                coupling_term += quantum_coupling
                
                result += coupling_term
                
        # Stochastic noise with fractal characteristics and quantum fluctuations
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.stochastic_noise_levels[i]
            
            # Fractal noise component with multi-scale influence and quantum modulation
            noise_component = noise_level * np.sin(10.0 * xi) * np.cos(5.0 * xi)
            noise_component += 0.3 * np.sin(20.0 * xi) * np.cos(10.0 * xi)
            
            # Quantum fluctuation term
            quantum_fluct = self.interference_strengths[i] * np.sin(7.0 * xi + self.quantum_phases[i]) * np.cos(7.0 * xi - self.quantum_phases[i])
            noise_component += 0.2 * quantum_fluct
            
            result += noise_component
            
        # Hill-climbing gradient with self-similar scaling and quantum effects
        for i in range(self.dim):
            xi = x[i]
            rate = self.hill_climbing_rates[i]
            
            # Self-similar hill-climbing component with quantum modulation
            hill_term = rate * np.exp(-xi**2 / 2) * (1.0 + 0.3 * np.sin(3 * xi))
            hill_term += 0.1 * self.interference_strengths[i] * np.cos(xi + self.quantum_phases[i])
            result += hill_term
            
        # Global scaling with fractal modulation and adaptive resonance
        global_factor = 1.0 + 0.5 * np.sin(np.sum(x) / self.dim)
        global_factor *= (1.0 + 0.2 * np.cos(2.0 * np.sum(x)))
        
        # Adaptive resonance factor
        adaptivity = 1.0 + 0.3 * np.sin(np.sum(x) * self.adaptivity_rates[0])
        global_factor *= adaptivity
        
        result *= global_factor
        
        return result